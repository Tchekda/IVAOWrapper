from .parser import Parser


class Server:
    clients = {}
    controllers = {}
    pilots = {}
    folme = {}

    def __init__(self):
        self.handlers = {}

    def call(self, type, *args):
        if type in self.handlers:
            for h in self.handlers[type]:
                h(*args)

    def event(self, type):
        def registerhandler(handler):
            if type in self.handlers:
                self.handlers[type].append(handler)
            else:
                self.handlers[type] = [handler]
            return handler

        return registerhandler

    def update_data(self):
        parser = Parser()
        for client in parser.get_clients_object():
            if client.vid not in Server.clients:
                self.call('newClient', client)
            Server.clients[client.vid] = client
            if client.client_type == "ATC":
                Server.controllers[client.vid] = client
            elif client.client_type == "PILOT":
                Server.pilots[client.vid] = client
            else:
                Server.folme[client.vid] = client
        self.call('updated')
