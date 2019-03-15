class Client:

    def __init__(self, callsign, vid, client_type, frequency=None):
        self.callsign = callsign
        self.vid = vid
        self.client_type = client_type
        self.frequency = frequency

    def __str__(self):
        return "{0} as {1} with {2} callsign".format(self.vid, self.client_type, self.callsign)
