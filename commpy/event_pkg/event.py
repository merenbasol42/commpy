from typing import Callable, Generic, Type, TypeVar
from .msg_if import MsgI
from ..std_ifs.msg import Empty
from ..utils import AlreadySubscribedError, NoConnectionError

# T is a generic type representing the message type of the event.
T = TypeVar('T', bound=MsgI)

class _Event:
    """
    A basic event class. Serves as the foundation for event-based communication.
    """
    def __init__(self, name: str):
        """
        Creates an event.

        Args:
            name (str): The name of the event.
        """
        self.name: str = name
        self.subscribers: list[Callable] = []

    def subscribe(self, callback: Callable, name: str = "Unnamed Subscriber"):
        """
        Subscribes a callback function to the event.

        Args:
            callback (Callable): The function to be called when the event is triggered.
            name (str, optional): The name of the subscriber. Defaults to "Unnamed Subscriber".

        Raises:
            AlreadySubscribedError: If the subscriber is already registered.
        """
        if callback in self.subscribers:
            raise AlreadySubscribedError(f"Callback '{name}' already subscribed to the event '{self.name}'.")

        self.subscribers.append(callback)

    def trigger(self, *args, triggerer: str = "Unnamed Triggerer", safe: bool = True):
        """
        Triggers the event and notifies all subscribers.

        Args:
            *args: Arguments to pass to the callback functions.
            triggerer (str, optional): The name of the entity triggering the event. Defaults to "Unnamed Triggerer".
            safe (bool, optional): Safe mode. Raises an error if no subscribers exist. Defaults to True.

        Raises:
            NoConnectionError: If no subscribers exist and safe=True.
        """
        if safe and not self.subscribers:
            raise NoConnectionError(f"Event '{self.name}' triggered by '{triggerer}' has no subscribers.")

        for subscriber in self.subscribers:
            try:
                subscriber(*args)
            except Exception as e:
                print(f"Error while notifying subscriber: {e}")

class Event(_Event, Generic[T]):
    """
    An event class extended with a specific message type.
    """
    def __init__(self, name: str, msg_type: Type[T] = Empty):
        """
        Creates an event with a message type.

        Args:
            name (str): The name of the event.
            msg_type (Type[T], optional): The type of the message. Defaults to Empty.
        """
        super().__init__(name)
        self.msg_type: Type[T] = msg_type

    def subscribe(self, callback: Callable[[T], None], name: str = "Unnamed Subscriber"):
        """
        Subscribes a callback function to the event.

        Args:
            callback (Callable[[T], None]): The function to be called when the event is triggered.
            name (str, optional): The name of the subscriber. Defaults to "Unnamed Subscriber".

        Raises:
            AlreadySubscribedError: If the subscriber is already registered.
        """
        super().subscribe(callback, name=name)

    def trigger(self, message: T, triggerer: str = "Unnamed Triggerer", safe: bool = True):
        """
        Triggers the event and notifies all subscribers.

        Args:
            message (T): The message to pass to the subscribers.
            triggerer (str, optional): The name of the entity triggering the event. Defaults to "Unnamed Triggerer".
            safe (bool, optional): Safe mode. Raises an error if no subscribers exist. Defaults to True.

        Raises:
            NoConnectionError: If no subscribers exist and safe=True.
        """
        super().trigger(message, triggerer=triggerer, safe=safe)

if __name__ == "__main__":
    class CustomMessage(MsgI):
        def __init__(self, content: str):
            self.content = content

    def example_callback(message: CustomMessage):
        print(f"Callback received message: {message.content}")

    # Create an Event.
    event = Event("ExampleEvent", msg_type=CustomMessage)

    # Subscribe the callback.
    event.subscribe(example_callback, name="ExampleCallback")

    # Trigger the event.
    test_message = CustomMessage("Hello, World!")
    event.trigger(test_message, triggerer="Main Function")