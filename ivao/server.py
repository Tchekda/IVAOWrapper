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
        data = parser.get_clients_object()
        for client in data['atc']:
            Server.controllers[client.vid] = client
            Server.clients[client.vid] = client
        for client in data['pilot']:
            Server.pilots[client.vid] = client
            Server.clients[client.vid] = client
        for client in data['folme']:
            Server.folme[client.vid] = client
            Server.clients[client.vid] = client
        self.call('updated')
