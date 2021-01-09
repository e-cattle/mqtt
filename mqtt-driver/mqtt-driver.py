#!/usr/bin/env python3

import json
from datetime import datetime

import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import redis
import requests

data = {
    "mac": "",
    "token": "",
    "measures": [{
        "name": "",
        "value": "",
        "date": "",
        "resource": ""
    }]
}

#bigboxx = "192.168.0.11"
bigboxx = "127.0.0.1"
api_port = 3000
api = f"http://{bigboxx}:{api_port}/"
rdb = redis.Redis(host=bigboxx)

response_topic = "Embrapa/Response/"
subscribe_topic = "#"

session = requests.Session()
headers = {'Content-Type': 'application/json'}


def get_date():
    now = datetime.now()
    return str(now.strftime("%d%m%y%H%M%S"))


def is_json(myjson):
    try:
        json_obj = json.loads(myjson)
        return True
    except ValueError as e:
        return False


def get_message(message):
    topic = str(message.topic)
    sensor = topic.split("/")

    # Embrapa/Response/aa:bb:cc:11:22:33
    if topic.__contains__('Response'):
        return

    # Embrapa/Contract/aa:bb:cc:11:22:33
    elif topic.__contains__('Contract'):
        contract = json.loads(str(message.payload.decode("utf-8")))

        # POST de requisição do contrato
        response = session.post(api + "device", headers=headers, data=json.dumps(contract))

        tk = json.loads(response.text)
        rdb.mset({sensor[2]: tk["token"]})

        # Informa o HTTP Status Code da requisição de contrato
        publish.single(response_topic + sensor[2], response.status_code, hostname=bigboxx)

        return

    # Embrapa/aa:bb:cc:11:22:33/sensor_name/resource
    else:
        # Atualiza o JSON de dados
        data["mac"] = sensor[1]
        token = rdb.get(sensor[1])

        if token.__str__() == 'None':
            data["token"] = "Null"
        else:
            data["token"] = bytes.decode(token)
        data["measures"][0]["name"] = str(sensor[2])
        data["measures"][0]["date"] = get_date()

        # Possui resource
        if len(sensor) == 4:
            data["measures"][0]["resource"] = sensor[3]

        # É Json
        msg = str(message.payload.decode("utf-8"))
        if is_json(msg) and isinstance(msg, float):
            data["measures"][0].update(json.loads(msg))
        else:
            data["measures"][0]["value"] = msg

        # POST de Dados
        response = session.post(api + "measure", headers=headers, data=json.dumps(data))

        # Apaga conteudo Json
        data.fromkeys(data, )

        # HTTP Codes API
        # 201 - Mensagem processada com sucesso
        # 401 - Token válido
        # 404 - Disp. bloqueado, Dados sens. ou tipo de sensor
        # 500 - Erro de processamento
        # Se contrato for inválido, informa o sensor
        if not response.status_code == 201:
            publish.single(response_topic + sensor[1], response.status_code, hostname=bigboxx)


def on_message(client, userdata, message):
    get_message(message)


if __name__ == '__main__':
    while True:
        subscribe.callback(on_message, subscribe_topic, hostname=bigboxx)
