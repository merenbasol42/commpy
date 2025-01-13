from typing import TypeVar, Generic, Type
from ..utils import AlreadyHasAServer, UnmatchingMsgType, NoConnectionError, type_check
from .client import _Client, Client
from .server import _Server, Server
from .srv_if import SrvMsgI

class _Service:
    def __init__(self, name: str):
        self.name = name
        self.server: _Server = None
        self.clients: list[_Client] = []

    def _cb(self, index: int, *args):
        response = self.server.serve(*args)
        self.clients[index].response = response

    def add_client(self, client: _Client):
        index = len(self.clients)
        def cb(*args): self._cb(index, *args)       
        client.e_call.subscribe(cb)
        self.clients.append(client)

    def add_service(self, server: _Server):
        if self.server != None: 
            raise AlreadyHasAServer(
                "This service already has a server"
            )
        self.server = server



T = TypeVar('T', bound=SrvMsgI)
TRequest = TypeVar('TRequest', bound=SrvMsgI.Request)
TResponse = TypeVar('TResponse', bound=SrvMsgI.Response)

class Service(_Service, Generic[T]):
    def __init__(self, type: Type[T], name: str = "none"):
        self.type = type
        self.server: Server[T]
        super().__init__(name)

    def _cb(self, index: int, req: TRequest):
        res = self.server.type.Response()
        if self.server is None:
            raise NoConnectionError(
                f"[on {self.name} named service] server is None"
            )
        if res != self.server.serve(req, res):
            raise Exception(
                f"[on {self.name} named service] serve method did not return response what given him"
            )
        type_check(self.type.Response, res)
        self.clients[index].response = res

    def add_client(self, client: Client[T]):
        if client.type != self.type:
            raise UnmatchingMsgType(
                expected = self.type,
                received = client.type
            )
        return super().add_client(client)

    def add_service(self, server: Server[T]):
        if server.type != self.type:
            raise UnmatchingMsgType(
                expected = self.type,
                received = server.type
            )
        return super().add_service(server)
