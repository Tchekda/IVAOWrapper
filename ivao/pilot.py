from .client import Client


class Pilot(Client):

    def __init__(self, callsign, vid, latitude, longitude, altitude, server, connection_time, soft_name, soft_version,
                 admin_rating, client_rating, groundspeed, aircraft, cruise_speed, departure_airport, cruise_level,
                 destination_airport, transponder, flight_rule, departure_time, actual_departure_time,
                 alternate_airport, fpl_remark, route, flight_type, passengers, heading, ground, simulator):
        super().__init__(callsign, vid, destination_airport, latitude, longitude, altitude, server, connection_time,
                         soft_name,
                         soft_version, admin_rating, client_rating)
        self.simulator = simulator
        self.ground = ground
        self.heading = heading
        self.passengers = passengers
        self.flight_type = flight_type
        self.groundspeed = int(groundspeed)
        self.aircraft = int(aircraft)
        self.cruise_speed = cruise_speed
        self.atis = departure_airport
        self.atis_time = cruise_level
        self.transponder = transponder
        self.flight_rule = flight_rule
        self.departure_time = departure_time
        self.actual_departure_time = actual_departure_time
        self.alternate_airport = alternate_airport
        self.fpl_remark = fpl_remark
        self.route = route

    def get_simulator_name(self):
        return {
            0: "Unknown",
            1: "Microsoft Flight Simulator 95",
            2: "Microsoft Flight Simulator 98",
            3: "Microsoft Combat Flight Simulator",
            4: "Microsoft Flight Simulator 2000",
            5: "Microsoft Combat Flight Simulator 2",
            6: "Microsoft Flight Simulator 2002",
            7: "Microsoft Combat Flight Simulator 3",
            8: "Microsoft Flight Simulator 2004",
            9: "Microsoft Flight Simulator X",
            11: "X-Plane",
            12: "X-Plane 8",
            13: "X-Plane 9",
            14: "X-Plane 10",
            15: "PS1",
            16: "X-Plane 11",
            17: "X-Plane 12",  # Really???
            20: "Fly!",
            21: "Fly! 2",
            25: "Prepar3D"
        }.get(self.simulator, 'Unknown')

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
            2: "Basic Flight Student (FS1)",
            3: "Flight Student (FS2)",
            4: "Advanced Flight Student (FS3)",
            5: "Private Pilot (PP)",
            6: "Senior Private Pilot (SPP)",
            7: "Commercial Pilot (CP)",
            8: "Airline Transport Pilot (ATP)",
            9: "Senior Flight Instructor (SFI)",
            10: "Chief Flight Instructor (CFI)"
        }.get(self.client_rating, None)
