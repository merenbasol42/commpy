from typing import Type
from ..utils import UnmatchingMsgType
from .srv_if import SrvMsgI

class _Server:
    def __init__(self, cb, name:str = "nameless server"):
        self.cb = cb
        self.name = name
    
    def serve(self, *args):
        self.cb(*args)

class Server(_Server):
    def __init__(self, srv_type: Type[SrvMsgI], cb, name: str = "nameless server"):
        self.type: Type[SrvMsgI] = srv_type
        super().__init__(cb, name)
    
    def serve(self, msg: SrvMsgI):
        if not isinstance(msg, self.type):
            raise UnmatchingMsgType(self.type, msg)
        return super().serve(msg) 
