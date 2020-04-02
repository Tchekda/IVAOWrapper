from ivao import Server

server = Server()


@server.event("update")
def get_data(clients):
    count = {
        'pilots' : 0,
        'ground' : 0,
        'air' : 0,
        'atc': 0,
        'folme' : 0
    }

    for _, client in clients.items():
        if client.client_type == "PILOT":
            count['pilots'] += 1
            if client.ground:
                count['ground'] += 1
            else:
                count['air'] += 1
        elif client.client_type == "ATC":
            count['atc'] += 1
        elif client.client_type == "":
            count['atc'] += 1

    print("{} on ground and {} in air for {} pilots".format(ground, air, pilots))


@server.event("land")
def land(client):
    print(client, " has land")


@server.event("static")
def static(client):
    print(client, " is static on " + ("ground" if client.ground else "air"))


@server.event("moving")
def moving(client):
    print(client, " is moving on " + ("ground" if client.ground else "air"))


@server.event("takeoff")
def land(client):
    print(client, " has takeoff")


@server.event("atis_update")
def atis(client):
   print(client, " has changed his ATIS")


@server.event("connect")
def connect(client, first_run):
    if first_run:
        pass
    else:
        print(client, " just connected")


@server.event("disconnect")
def disconnect(client):
    print(client, " just disconnected")


server.run_update_stream(delay=0.5)
