import grpc
from concurrent import futures
import market_pb2
import market_pb2_grpc

class MarketService(market_pb2_grpc.MarketServiceServicer):
    def __init__(self):
        self.items = {}  # Placeholder for storing item details
        
    def NotifyClient(self, request, context):
        updated_item = request.updated_item

        print("#######")
        print("The Following Item has been updated:")
        print(f"Item ID: {updated_item.id}, Price: ${updated_item.price}, Name: {updated_item.name}, "
              f"Category: {updated_item.category},")
        print(f"Description: {updated_item.description}, Quantity Remaining: {updated_item.quantity_remaining}")
        print(f"Rating: {updated_item.rating} / 5 | Seller: {updated_item.seller}")
        print(f"Recipient Type: {request.recipient_type}")  # Print recipient type
        print("#######")

        response = market_pb2.NotifyClientResponse(result="SUCCESS")
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    market_pb2_grpc.add_MarketServiceServicer_to_server(MarketService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Market server started on port 50052")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
