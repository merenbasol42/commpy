from ..utils import AlreadyHasAServer, UnmatchingMsgType
from .client import __Client, Client
from .server import __Server, Server
from .srv_if import SrvMsgI

class __Service:
    def __init__(self, name: str):
        self.name = name
        self.server: __Server = None
        self.clients: list[__Client] = []

    def __cb(self, index: int, *args):
        response = self.server.cb(*args)
        self.clients[index].response = response

    def add_client(self, client: __Client):
        index = len(self.clients)
        def cb(*args): self.__cb(index, *args)       
        client.e_call.subscribe(cb)
        self.clients.append(client)

    def add_service(self, server: __Server):
        if self.server != None: raise AlreadyHasAServer(
            "This service already has a server"
        )
        self.server = server

class Service(__Service):
    def __init__(self, type: type[SrvMsgI], name: str = "none"):
        self.type = type
        super().__init__(name)

    def add_client(self, client: Client):
        if client.type != self.type:
            raise UnmatchingMsgType(
                expected = self.type,
                received = client.type
            )
        return super().add_client(client)

    def add_service(self, server: Server):
        if server.type != self.type:
            raise UnmatchingMsgType(
                expected = self.type,
                received = server.type
            )
        return super().add_service(server)