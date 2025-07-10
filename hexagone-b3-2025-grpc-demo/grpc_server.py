from interface_pb2_grpc import GreeterServicer, add_GreeterServicer_to_server
from interface_pb2 import HelloReply


import grpc
from concurrent import futures

class GreeterServer(GreeterServicer):

    def SayHello(self, request, context):
        return HelloReply(message='Hello from the moon')

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_GreeterServicer_to_server(GreeterServer(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

serve()