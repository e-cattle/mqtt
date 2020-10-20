class Contextual:
    def __init__(self, resource, date):
        self.resource = resource
        self.date = date


class Gateopened(Contextual):
    def __init__(self, resource, date, value=False):
        super().__init__(resource, date)
        self.value = value


class Geographiccoordinate(Contextual):
    def __init__(self, altitude, latitude, longitude, resource, date):
        super().__init__(resource, date)
        self.altitude = altitude
        if latitude < -90:
            self.latitude = -90
        elif latitude > 90:
            self.latitude = 90
        else:
            self.latitude = latitude

        if longitude < -180:
            self.longitude = -180
        elif longitude > 180:
            self.longitude = 180
        else:
            self.longitude = longitude
