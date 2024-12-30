import grpc
from concurrent import futures
import messaging_pb2 as messaging_pb2
import messaging_pb2_grpc as messaging_pb2_grpc
from grpc_reflection.v1alpha import reflection

class MessagingServiceServicer(messaging_pb2_grpc.MessagingServiceServicer):
    def SendMessage(self, request, context):
        print(f"Received message: {request.text}")
        return messaging_pb2.Message(text=f"Server received: {request.text}")


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    messaging_pb2_grpc.add_MessagingServiceServicer_to_server(MessagingServiceServicer(), server)
    SERVICE_NAMES = (
        messaging_pb2.DESCRIPTOR.services_by_name['MessagingService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:8022')
    server.start()
    print("Server started on port 8022 with reflection enabled")
    server.wait_for_termination()

if __name__ == '__main__':
    main()
