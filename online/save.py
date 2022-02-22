from json import load, dump
from server import Server
uuid_file = "/online/servers.json"


def server_import():
    """Return servers in uuid.json"""
    servers = []
    with open(uuid_file, "r") as file:
            srv_list = load(file)
            for ip in key(jfile):
                servers.append(Server(
                    ip = ip,
                    name = srv_list[ip]['name'],
                    uuid = srv_list[ip]['uuid']))

    return servers

def server_export(server: Server):
    """Add a new server to the server list"""
    file = open(uuid_file, "r")
    srv_list = load(file)
    file.close()

    srv_list.update(server)

    with open(uuid_file, "w") as file:
        file.write(srv_list)
