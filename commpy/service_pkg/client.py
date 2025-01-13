import time
from ..utils import NoConnectionError, type_check
from ..event_pkg import Event
from .srv_if import SrvMsgI
from typing import Type, Generic, TypeVar

ZZZ_TIME: float = 0.05

class _Client:
    def __init__(self, name: str = "nameless client"):
        self.e_call: Event = Event(f"__{name} client call__")
        self.response = None

    def call_sync(self, *args):
        if len(self.e_call.get_subs()) == 0: 
            raise NoConnectionError("this client has not connection but want to call")
        self.response = None
        self.e_call.trigger(*args)
        while self.response == None:
            time.sleep(ZZZ_TIME)
        return self.response

T = TypeVar('T', bound=SrvMsgI)
TRequest = TypeVar('TRequest', bound=SrvMsgI.Request)
TResponse = TypeVar('TResponse', bound=SrvMsgI.Response)

class Client(_Client, Generic[T]):
    def __init__(self, srv_type: Type[T], name: str = "nameless client"):
        self.type: Type[T] = srv_type  # Tip bilgisini sakla
        super().__init__(name)
        
    def call_sync(self, msg: TRequest) -> TResponse:
        type_check(self.type.Request, msg)
        return super().call_sync(msg)
        