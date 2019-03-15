from .Client import Client


class Parser:

    def __init__(self):
        with open('whazzup.2.txt') as file:
            self.content = file.read()
        self.clients = self.content.split('!CLIENTS\n')[1].split('!AIRPORTS')[0].split('\n')[:-1]

    def get_raw_data(self):
        return self.content

    def get_clients_object(self):
        users = []
        for client in self.clients:
            data = client.split(':')
            users.append(Client(callsign=data[0], vid=data[1], client_type=data[3], frequency=data[4]))
        return users