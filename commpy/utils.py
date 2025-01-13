class CommError(Exception): pass

class UnmatchingMsgType(CommError): 
    def __init__(self, expected: type, received: type, *args):
        super().__init__(
            str(f"expected: {expected}, received: {received}"), 
            *args
        )
        
class AlreadySubscribedError(CommError): pass

class AlreadyHasAServer(CommError): pass

class NoConnectionError(CommError): pass

def type_check(expected: type, received: object):
    """Raises a UnmatchingMsgType error if the received object's type does not match the expected type.

    Args:
        expected: The expected type of the object.
        received: The object to check.

    Raises:
        UnmatchingMsgType: If the type of the received object does not match the expected type.  The exception includes the expected and received types.
    """
    if not isinstance(received, expected):
        raise UnmatchingMsgType(expected, received)
