class Server:
    """Load a server"""
    def __init__(self, ip : str, name : str, port : int, uuid = None):
        self.ip = ip
        self.name = name
        self.port = port
        self.uuid = uuid
