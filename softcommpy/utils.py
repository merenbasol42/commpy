class CommError(Exception): pass

class UnmatchingMsgType(CommError): 
    def __init__(self, expected: type, received: object, *args):
        super().__init__(
            str(f"expected: {expected}, received: {type(received)}"), 
            *args
        )
        
class AlreadySubscribedError(CommError): pass

class AlreadyHasAServer(CommError): pass

class NoConnectionError(CommError): pass
