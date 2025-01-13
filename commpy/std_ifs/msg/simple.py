from ...event_pkg.msg_if import MsgI
from typing import Generic, TypeVar

T = TypeVar('T')

class MTSimple(MsgI, Generic[T]):  # MTList generic bir sınıf
    def __init__(self, data: T):
        self.data: T 
        super().__init__(data=data)  