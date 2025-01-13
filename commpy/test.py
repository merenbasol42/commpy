from commpy.service_pkg import Client, Server, Service
from commpy.std_ifs.srv import Add

class ExampleServer:
    def __init__(self):
        self.srv = Server(Add, self.srv_cb, "ex_server")

    def srv_cb(self, req: Add.Request, res: Add.Response) -> Add.Response:
        count: int = 0
        for n in req.numbers:
            count += n
        res.sum = count
        return res

class ExampleClient:
    def __init__(self):
        self.client = Client(Add, name="ex_cli")

    def call_trigger(self):
        # req = Add.Request(numbers=[1, 2, 3])
        req = Add.Request()
        req.numbers = [1, 2, 3]
        res: Add.Response = self.client.call_sync(req)
        print(f"response is {res.sum}")

class ExampleService:
    def __init__(self):
        self.service = Service(Add, "Adding Service 1")
        self.a = ExampleServer()
        self.b = ExampleClient()
        self.service.add_service(self.a.srv)
        self.service.add_client(self.b.client)

def test():
    c = ExampleService()
    c.b.call_trigger()

if __name__ == "__main__":
    test()

