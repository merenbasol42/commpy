from ...service_pkg.srv_if import SrvMsgI as _SrvMsgI
from ..msg import ListInt as _ListInt
from ..msg import Int as _Int 

class Add(_SrvMsgI):
    def __init__(self):
        self.request: _ListInt = _ListInt()
        self.response: _Int = _Int()
        super().__init__()
