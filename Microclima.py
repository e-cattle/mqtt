class Microclima:
    def __init__(self, resource, date):
        self.resource = resource
        self.date = date


class AirTemperature(Microclima):
    def __init__(self, value, resource, date, unit='C'):
        super().__init__(resource, date)
        self.unit = unit
        if value < -99:
            self.value = -99
        elif value > 1999:
            self.value = 1999
        else:
            self.value = value


class BlackGlobeTemperature(Microclima):
    def __init__(self, value, resource, date, unit='C'):
        super().__init__(resource, date)
        self.unit = unit
        if value < -50:
            self.value = -50
        elif value > 100:
            self.value = 100
        else:
            self.value = value


class CH4(Microclima):
    def __init__(self, value, resource, date, unit='ppm'):
        super().__init__(resource, date)
        self.unit = unit
        self.value = value


class CO2(Microclima):
    def __init__(self, value, resource, date, unit='ppm'):
        super().__init__(resource, date)
        self.unit = unit
        self.value = value


class DewPointTemperature(Microclima):
    def __init__(self, value, resource, date, unit='C'):
        super().__init__(resource, date)
        self.unit = unit
        if value < -50:
            self.value = -50
        elif value > 100:
            self.value = 100
        else:
            self.value = value


class DryBulbTemperature(Microclima):
    def __init__(self, value, resource, date, unit='C'):
        super().__init__(resource, date)
        self.unit = unit
        if value < -50:
            self.value = -50
        elif value > 100:
            self.value = 100
        else:
            self.value = value


class PH(Microclima):
    def __init__(self, value, resource, date, unit='pH'):
        super().__init__(resource, date)
        self.unit = unit
        if value < 0:
            self.value = 0
        elif value > 14:
            self.value = 14
        else:
            self.value = value


class Precipitation(Microclima):
    def __init__(self, value, resource, date, unit='mm'):
        super().__init__(resource, date)
        self.unit = unit
        if value < 0:
            self.value = 0
        else:
            self.value = value


class RelativeHumidity(Microclima):
    def __init__(self, value, resource, date, unit='%'):
        super().__init__(resource, date)
        self.unit = unit
        if value < 0:
            self.value = 0
        elif value > 100:
            self.value = 100
        else:
            self.value = value


class SoilNitrogen(Microclima):
    def __init__(self, value, resource, date, unit='C'):
        super().__init__(resource, date)
        self.unit = unit
        if value < 0:
            self.value = 0
        elif value > 100:
            self.value = 100
        else:
            self.value = value


class SoilMoisture(Microclima):
    def __init__(self, value, resource, date, unit='%'):
        super().__init__(resource, date)
        self.unit = unit
        if value < 0:
            self.value = 0
        elif value > 100:
            self.value = 100
        else:
            self.value = value


class SoilWaterPotencial(Microclima):
    def __init__(self, value, resource, date, unit='Cbar'):
        super().__init__(resource, date)
        self.unit = unit
        if value < 0:
            self.value = 0
        elif value > 250:
            self.value = 250
        else:
            self.value = value


class SolarRadiation(Microclima):
    def __init__(self, value, resource, date, unit='W/m2'):
        super().__init__(resource, date)
        self.unit = unit
        if value < 0:
            self.value = 0
        elif value > 1500:
            self.value = 1500
        else:
            self.value = value


class WaterTemperature(Microclima):
    def __init__(self, value, resource, date, unit='C'):
        super().__init__(resource, date)
        self.unit = unit
        if value < 0:
            self.value = 0
        elif value > 100:
            self.value = 100
        else:
            self.value = value


class WetBulbTemperature(Microclima):
    def __init__(self, value, resource, date, unit='C'):
        super().__init__(resource, date)
        self.unit = unit
        if value < 0:
            self.value = 0
        elif value > 40:
            self.value = 40
        else:
            self.value = value


class WindSpeed(Microclima):
    def __init__(self, speed, direction, resource, date, unit='m/s'):
        super().__init__(resource, date)
        self.unit = unit
        self.direction = direction
        if speed < 0:
            self.speed = 0
        elif speed > 125:
            self.speed = 125
        else:
            self.speed = speed
