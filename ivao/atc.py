from .client import Client


class Controller(Client):

    def __init__(self, callsign, vid, latitude, longitude, altitude, server, connection_time, soft_name, soft_version,
                 admin_rating, client_rating, frequencies, facility, visual_range, atis, atis_time, client_type):
        super().__init__(callsign, vid, client_type, latitude, longitude, altitude, server, connection_time, soft_name,
                         soft_version, admin_rating, client_rating)
        self.frequencies = frequencies.split("&")
        self.facility = int(facility)
        self.visual_range = float(visual_range)
        self.atis = atis
        self.atis_time = atis_time

    def get_facility_name(self):
        return {
            0: "Observer",
            1: "Flight Information",
            2: "Delivery",
            3: "Ground",
            4: "Tower",
            5: "Approach",
            6: "Area Control Centre",
            7: "Departure"
        }.get(self.facility, None)

    def get_admin_rating_name(self):
        return {
            0: "Suspended",
            1: "Observer",
            2: "User",
            11: "Supervisor",
            12: "Administrator",
        }.get(self.admin_rating, None)

    def get_client_rating_name(self):
        return {
            1: "Observer",
            2: "ATC Applicant (AS1)",
            3: "ATC Trainee (AS2)",
            4: "Advanced ATC Trainee (AS3)",
            5: "Aerodrome Controller (ADC)",
            6: "Approach Controller (APC)",
            7: "Center Controller (ACC)",
            8: "Senior Controller (SEC)",
            9: "Senior ATC Instructor (SAI)",
            10: "Chief ATC Instructor (CAI)"
        }.get(self.client_rating, None)
