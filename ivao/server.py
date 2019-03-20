import random
import threading
import time

from .parser import Parser


class Server:

    def __init__(self):
        self.handlers = {}
        self.clients = {}
        self.controllers = {}
        self.pilots = {}
        self.folme = {}
        self.update_stream = threading.currentThread()

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
            if client.vid in self.controllers and self.controllers[client.vid].atis_time != client.atis_time:
                self.call("atis_update", client)
            self.controllers[client.vid] = client
            self.clients[client.vid] = client
        for client in data['pilot']:
            if client.vid in self.pilots and self.pilots[client.vid].ground != client.ground:
                if client.ground:
                    self.call("land", client)
                else:
                    self.call("takeoff", client)
            self.pilots[client.vid] = client
            self.clients[client.vid] = client
        for client in data['folme']:
            self.folme[client.vid] = client
            self.clients[client.vid] = client
        self.call('updated', self.clients)

    def stop_update_stream(self):
        self.update_stream.do_run = False

    def run_update_stream(self, delay=None):
        while getattr(self.update_stream, "do_run", True):
            self.update_data()
            if delay:
                time.sleep(delay * 60)
            else:
                time.sleep(random.randint(1, 3) * 60)
