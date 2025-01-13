from ...service_pkg.srv_if import SrvMsgI as _SrvMsgI

class Add(_SrvMsgI):
    class Request(_SrvMsgI.Request):
        def __init__(self, numbers: list[int] = []):
            self.numbers: list[int]
            super().__init__(numbers=numbers)

    class Response(_SrvMsgI.Response):
        def __init__(self, sum: int = 0):
            self.sum: int
            super().__init__(sum=sum)

