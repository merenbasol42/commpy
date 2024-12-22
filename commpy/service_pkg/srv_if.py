from ..msg_if import MsgI

class SrvMsgI:
    def __init__(self):
        self.request: MsgI
        self.response: MsgI