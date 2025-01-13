from typing import Type, Generic, TypeVar
from ..utils import UnmatchingMsgType
from .srv_if import SrvMsgI

class _Server:
    def __init__(self, cb, name:str = "nameless server"):
        self.cb = cb
        self.name = name
    
    def serve(self, *args):
        return self.cb(*args)

T = TypeVar('T', bound=SrvMsgI)
TRequest = TypeVar('TRequest', bound=SrvMsgI.Request)
TResponse = TypeVar('TResponse', bound=SrvMsgI.Response)

class Server(_Server, Generic[T]):
    def __init__(self, srv_type: Type[T], cb, name: str = "nameless server"):
        self.type: Type[T] = srv_type
        super().__init__(cb, name)
    
    def serve(self, req: TRequest, res: TResponse) -> TResponse:
        if not isinstance(req, self.type.Request):
            raise UnmatchingMsgType(self.type.Request, req)
        return super().serve(req, res) 
