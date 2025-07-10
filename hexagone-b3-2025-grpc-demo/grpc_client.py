import grpc
from interface_pb2_grpc import GreeterStub
from interface_pb2 import HelloRequest

with grpc.insecure_channel('localhost:50051') as channel:
    stub = GreeterStub(channel)
    response = stub.SayHello(HelloRequest(name='Super astronaute'))
    print(response.message)