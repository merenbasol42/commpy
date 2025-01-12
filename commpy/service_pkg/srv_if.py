# srv_if.py
from ..msg_if import MsgI

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

class SrvMsgI:
    class Request(Request):
        pass

    class Response(Response):
        pass