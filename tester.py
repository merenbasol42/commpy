from softcommpy.service_pkg import Server, Client, Service
from softcommpy.std_ifs.srv import Add

def srv_cb(msg: Add):
    count: int = 0
    for num in msg.request.data:
        count += num
    msg.response.data = count
    return msg

service = Service(Add)
server = Server(Add, srv_cb)
client = Client(Add)
service.add_service(server)
service.add_client(client)

msg = Add()
msg.request.data = [7, 8, 2, 3]
print(client.call_sync(msg).response.data)