import time
from ..utils import UnmatchingMsgType
from ..event_pkg import Event
from .srv_if import SrvMsgI
from typing import Type

ZZZ_TIME: float = 0.05

class __Client:
    def __init__(self, name: str = "nameless client"):
        self.e_call: Event = Event(f"{name} client call")
        self.response = None

    def call_sync(self, *args):
        self.response = None
        self.e_call.trigger(*args)
        while self.response == None:
            time.sleep(ZZZ_TIME)
        return self.response

class Client(__Client):
    def __init__(self, srv_type: Type[SrvMsgI], name = "nameless client"):
        self.type: SrvMsgI = srv_type
        super().__init__(name)

    def call_sync(self, msg: SrvMsgI) -> SrvMsgI:
        if not isinstance(msg, self.type): 
            raise UnmatchingMsgType()
        return super().call_sync(msg)
