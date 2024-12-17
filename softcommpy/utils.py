class CommError(Exception): pass

class UnmatchingMsgType(CommError): 
    def __init__(self, expected, received, *args):
        super().__init__(
            str(f"expected: {type(expected)}, received: {type(received)}"), 
            *args
        )

class AlreadyHasAServer(CommError): pass