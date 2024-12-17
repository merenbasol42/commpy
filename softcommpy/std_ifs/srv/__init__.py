from ...service_pkg.srv_if import SrvMsgI as __SrvMsgI
from ..msg import ListInt as __ListInt
from ..msg import Int as __Int 

class Add(__SrvMsgI):
    def __init__(self):
        self.request: __ListInt = __ListInt()
        self.response: __Int = __Int()
        super().__init__()
