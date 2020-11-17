import json
import redis
import requests
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
from datetime import datetime

data = {
    "mac": "",
    "token": "",
    "measures": {
        "name": "",
        "value": "",
        "date": "",
        "resource": ""
    }
}

bigboxx = "192.168.0.11"
api_port = 3000
api = f"http://{bigboxx}:{api_port}/"
r = redis.Redis(host=bigboxx)

session = requests.Session()


def get_date():
    now = datetime.now()
    return str(now.strftime("%d%m%y%H%M%S"))


def get_message(message):
    topic = str(message.topic)
    sensor = topic.split("/")

    # Embrapa/Response/aa:bb:cc:11:22:33
    if topic.__contains__('Response'):
        return

    # Embrapa/Contract/aa:bb:cc:11:22:33
    elif topic.__contains__('Contract'):
        contract = json.loads(message.payload.decode("utf-8"))

        # POST de requisição do contrato
        result = session.post(str(api) + "devices", data=contract)

        # Guarda o Token gerado no banco REDIS
        r.mset({sensor[2]: "TOKEN"})

        # Informa o HTTP Status Code da requisição de contrato
        publish.single("Embrapa/Response/" + sensor[2], result.status_code, hostname=bigboxx)

    # Embrapa/aa:bb:cc:11:22:33/sensor_name/resource
    else:
        # Atualiza o JSON de dados
        data["mac"] = sensor[1]
        data["token"] = r.get(sensor[1])
        data["measures"]["name"] = sensor[2]
        data["measures"]["value"] = str(message.payload.decode("utf-8"))
        data["measures"]["date"] = get_date()
        if len(sensor) == 4:
            data["measures"]["resource"] = sensor[3]
        else:
            data["measures"]["resource"] = ""

        # POST de Dados
        result = session.post(str(api) + "measures", data=json.dumps(data))

        # HTTP Codes API
        # 201 - Mensagem processada com sucesso
        # 401 - Token válido
        # 404 - Disp. bloqueado, Dados sens. ou tipo de sensor
        # 500 - Erro de processamento
        # Se contrato for inválido, informa o sensor
        if not result.status_code == 201:
            publish.single("Embrapa/Response/" + sensor[1], result.status_code, hostname=bigboxx)


def on_message(client, userdata, message):
    get_message(message)


if __name__ == '__main__':
    while True:
        subscribe.callback(on_message, "#", hostname=bigboxx)