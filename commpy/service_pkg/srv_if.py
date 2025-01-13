# srv_if.py
from ..event_pkg.msg_if import MsgI

class SrvMsgI:
    class Request(MsgI):
        def __init__(self, **kwargs):
            super().__init__()
            for key, value in kwargs.items():
                setattr(self, key, value)

    class Response(MsgI):
        def __init__(self, **kwargs):
            super().__init__()
            for key, value in kwargs.items():
                setattr(self, key, value)
