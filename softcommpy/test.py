
from .service_pkg import Client, Server, Service
from .std_ifs.srv import Add

class ExampleServer:
    def __init__(self):
        self.srv = Server(Add, self.srv_cb, "ex_server")

    def srv_cb(self, msg: Add) -> Add:
        count: int = 0
        for n in msg.request.data:
            count += n
        msg.response.data = count
        return msg

class ExampleClient:
    def __init__(self):
        self.client = Client(Add, name="ex_cli")

    def call_trigger(self):
        msg: Add = Add()
        msg.request.data = [1, 2, 3]
        msg: Add = self.client.call_sync(msg)
        print(f"response is {msg.response.data}")

class ExampleService:
    def __init__(self):
        self.service = Service(Add, "Adding Service 1")
        self.a = ExampleServer()
        self.b = ExampleClient()
        print(self.service.server)
        self.service.add_service(self.a.srv)
        self.service.add_client(self.b.client)

def test():
    c = ExampleService()
    c.b.call_trigger()

if __name__ == "__main__":
    test()
