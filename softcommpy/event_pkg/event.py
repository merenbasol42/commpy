from ..msg_if import MsgI
from .utils import *

class __Event:
    def __init__(self, name: str):
        self.name: str = name
        self.subs: list = []
    
    def subscribe(self, cb, name: str = "nameless sub"):
        count: int = self.subs.count(cb)
        if count != 0: raise AlreadySubscribedError  

        self.subs.append(cb)

    def trigger(self, *args, triggerer: str = "nameless triggerer"):
        for sub in self.subs: 
            sub(*args)

class Event(__Event):
    def __init__(self, name, msg_type: type[MsgI]):
        self.type = msg_type
        super().__init__(name)
