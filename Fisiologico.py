class Fisiologico:
    def __init__(self, resource, date):
        self.resource = resource
        self.date = date


class AnimalWeight(Fisiologico):
    def __init__(self, value, resource, date, unit='Kg'):
        super().__init__(resource, date)
        if value < 0:
            self.value = 0
        elif value > 1999:
            self.value = 1999
        else:
            self.value = value
        self.unit = unit


class BodyTemperature(Fisiologico):
    def __init__(self, value, resource, date, unit='C'):
        super().__init__(resource, date)
        if value < 20:
            self.value = 20
        elif value > 50:
            self.value = 50
        else:
            self.value = value
        self.unit = unit


class HeartRate(Fisiologico):
    def __init__(self, value, resource, date, unit='bpm'):
        super().__init__(resource, date)
        if value < 0:
            self.value = 0
        elif value > 100:
            self.value = 100
        else:
            self.value = value
        self.unit = unit


class RespiratoryFrequency(Fisiologico):
    def __init__(self, value, resource, date, unit='bpm'):
        super().__init__(resource, date)
        if value < 0:
            self.value = 0
        elif value > 200:
            self.value = 200
        else:
            self.value = value
        self.unit = unit


class RetalTemperature(Fisiologico):
    def __init__(self, value, resource, date, unit='C'):
        super().__init__(resource, date)
        if value < 30:
            self.value = 30
        elif value > 45:
            self.value = 45
        else:
            self.value = value
        self.unit = unit
