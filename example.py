from ivao import Server, Client, Controller, Pilot
import os

server = Server()


@server.event("update")
def get_data(clients):
    count = {
        'pilots': 0,
        'ground': 0,
        'air': 0,
        'atc': 0,
        'folme': 0
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

    print(
        "{} pilots ({} ground / {} air) - {} ATC - {} Follow Me".format(count['pilots'], count['ground'], count['air'],
                                                                        count['atc'], count['folme']))


@server.event("static")
def static(client: Pilot):
    print(client, " is static on " + ("ground" if client.ground else "air"))


@server.event("moving")
def moving(client: Pilot):
    print(client, " is moving on " + ("ground" if client.ground else "air"))


@server.event("land")
def land(client: Pilot):
    print(client, " has land")


@server.event("takeoff")
def takeoff(client: Pilot):
    print(client, " has takeoff")


@server.event("cruise")
def cruise(client: Pilot):
    print(client, " is cruising at", client.altitude, "ft")


@server.event("climb")
def climb(client: Pilot):
    print(client, " is currently climbing")


@server.event("descent")
def descent(client: Pilot):
    print(client, " is currently descending")


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


if __name__ == "__main__":
    delay = None
    if os.getenv("UPDATE_DELAY") is not None:
        delay = float(os.getenv("UPDATE_DELAY"))
    server.run_update_stream(delay=delay)  # If None, a random value will be used
