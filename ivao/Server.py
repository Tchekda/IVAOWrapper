from .Parser import Parser


class Server:
    clients = []
    controllers = []
    pilots = []
    folme = []

    def __init__(self):
        self.update_data()

    def update_data(cls):
        parser = Parser()
        for client in parser.get_clients_object():
            if client not in cls.clients:
                cls.clients.append(client)
                if client.client_type == "ATC":
                    cls.controllers.append(client)
                elif client.client_type == "PILOT":
                    cls.pilots.append(client)
                else:
                    cls.folme.append(client)
