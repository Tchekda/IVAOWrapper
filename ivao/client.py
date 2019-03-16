import datetime


class Client:

    def __init__(self, callsign, vid, client_type, latitude, longitude, altitude, server, connection_time, soft_name,
                 soft_version, admin_rating, client_rating):
        self.callsign = callsign
        self.vid = int(vid)
        self.client_type = client_type
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = int(altitude)
        self.server = server
        self.connection_time = datetime.datetime(year=int(connection_time[:4]), month=int(connection_time[4:6]),
                                                 day=int(connection_time[6:8]), hour=int(connection_time[8:10]),
                                                 minute=int(connection_time[10:12]), second=int(connection_time[12:14]))
        self.soft_name = soft_name
        self.soft_version = soft_version
        self.admin_rating = int(admin_rating)
        self.client_rating = int(client_rating)

    def __str__(self):
        return "{0} as {1} with {2} callsign".format(self.vid, self.client_type, self.callsign)
