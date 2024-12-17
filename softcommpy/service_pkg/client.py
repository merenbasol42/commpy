import time
from ..utils import UnmatchingMsgType, NoConnectionError
from ..event_pkg import Event
from .srv_if import SrvMsgI
from typing import Type, Generic, TypeVar

ZZZ_TIME: float = 0.05

# TypeVar'ı belirli bir kısıtlama ile tanımla
SrvMsgT = TypeVar('SrvMsgT', bound=SrvMsgI)  # SrvMsgI türünden türeyen türler

class _Client:
    def __init__(self, name: str = "nameless client"):
        self.e_call: Event = Event(f"{name} client call")
        self._response = None

    def call_sync(self, *args):
        if len(self.e_call.subs) == 0: 
            raise NoConnectionError("this client has not connection but want to call")
        self._response = None
        self.e_call.trigger(*args)
        while self._response == None:
            time.sleep(ZZZ_TIME)
        return self._response

class Client(_Client, Generic[SrvMsgT]):
    def __init__(self, srv_type: Type[SrvMsgT], name: str = "nameless client"):
        self.type: Type[SrvMsgT] = srv_type  # Tip bilgisini sakla
        super().__init__(name)

    def call_sync(self, msg: SrvMsgT) -> SrvMsgT:
        if not isinstance(msg, self.type):
            raise UnmatchingMsgType(expected = self.type, received = msg)
        return super().call_sync(msg)  # Dönüş tipi SrvMsgT ile aynı
