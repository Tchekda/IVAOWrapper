from ivao import Server

server = Server()


@server.event("updated")
def get_data(clients):
    ground = 0
    air = 0
    pilots = 0
    for vid, client in clients.items():
        if client.client_type == "PILOT":
            pilots += 1
            if client.ground:
                ground += 1
            else:
                air += 1
    print("Data has been updated")
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
    # pass


server.run_update_stream(delay=0.5)
