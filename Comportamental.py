class Comportamental:
    def __init__(self, resource, date):
        self.resource = resource
        self.date = date


class Accelerometer(Comportamental):
    def __init__(self, ax, ay, az, resource, date):
        super().__init__(resource, date)
        self.ax = ax
        self.ay = ay
        self.az = az


class AnimalSpeed(Comportamental):
    def __init__(self, value, resource, date, unit='m/s'):
        super().__init__(resource, date)
        self.unit = unit
        if value < 0:
            self.value = 0
        elif value > 16:
            self.value = 16
        else:
            self.value = value



class Gyroscope(Comportamental):
    def __init__(self, gx, gy, gz, resource, date):
        super().__init__(resource, date)
        self.gx = gx
        self.gy = gy
        self.gz = gz


class Magnetometer(Comportamental):
    def __init__(self, mx, my, mz, resource, date):
        super().__init__(resource, date)
        self.mx = mx
        self.my = my
        self.mz = mz
