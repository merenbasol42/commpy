from ..msg_if import MsgI
from ..std_ifs.msg import Empty
from ..utils import AlreadySubscribedError, NoConnectionError

class _Event:
    def __init__(self, name: str):
        self.name: str = name
        self.subs: list = []
    
    def subscribe(self, cb, name: str = "nameless sub"):
        count: int = self.subs.count(cb)
        if count != 0: raise AlreadySubscribedError  

        self.subs.append(cb)

    def trigger(self, *args, triggerer: str = "nameless triggerer", safe = True):
        if safe: 
            if len(self.subs) == 0:
                raise NoConnectionError("this event has not a connection but want to trigger")
        for sub in self.subs: 
            sub(*args)

class Event(_Event):
    def __init__(self, name, msg_type: type[MsgI] = Empty):
        self.type = msg_type
        super().__init__(name)
