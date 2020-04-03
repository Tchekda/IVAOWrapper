from ivao import Server, Client, Controller, Pilot

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

    print("{} pilots ({} ground / {} air) - {} ATC - {} Follow Me".format(count['pilots'], count['ground'], count['air'], count['atc'], count['folme']))


@server.event("land")
def land(client: Pilot):
    print(client, " has land")


@server.event("static")
def static(client: Pilot):
    print(client, " is static on " + ("ground" if client.ground else "air"))


@server.event("moving")
def moving(client: Pilot):
    print(client, " is moving on " + ("ground" if client.ground else "air"))


@server.event("takeoff")
def land(client: Pilot):
    print(client, " has takeoff")


@server.event("atis_update")
def atis(client: Controller):
   print(client, " has changed his ATIS")


@server.event("connect")
def connect(client: Client, first_run: bool):
    if first_run:
        pass
    else:
        print(client, " just connected")


@server.event("disconnect")
def disconnect(client: Client):
    print(client, " just disconnected")


server.run_update_stream(delay=0.5)
