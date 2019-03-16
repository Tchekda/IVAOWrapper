class Client:

    def __init__(self, callsign, vid, client_type, latitude, longitude, altitude, server, connection_time, soft_name,
                 soft_version, admin_rating, client_rating):
        self.callsign = callsign
        self.vid = vid
        self.client_type = client_type
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.server = server
        self.connection_time = connection_time
        self.soft_name = soft_name
        self.soft_version = soft_version
        self.admin_rating = int(admin_rating)
        self.client_rating = int(client_rating)

    def __str__(self):
        return "{0} as {1} with {2} callsign".format(self.vid, self.client_type, self.callsign)
