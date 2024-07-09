import grpc
import buyer_pb2
import buyer_pb2_grpc
from concurrent import futures

class BuyerNotificationServer(buyer_pb2_grpc.BuyerServiceServicer):
    def NotifyItemUpdate(self, request, context):
        print("Received item update notification:")
        print(f"Item ID: {request.id}, Price: ${request.price}, Name: {request.name}, "
              f"Category: {request.category},")
        print(f"Description: {request.description}, Quantity Remaining: {request.quantity_remaining}")
        print(f"Seller: {request.seller}, Rating: {request.rating}")

        response = buyer_pb2.ItemNotificationResponse(result="SUCCESS")
        return response

def run_buyer_instance():
    
    buyer_channel = grpc.insecure_channel('localhost:50054')

    
    buyer_stub = buyer_pb2_grpc.BuyerServiceStub(buyer_channel)

    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    buyer_pb2_grpc.add_BuyerServiceServicer_to_server(BuyerNotificationServer(), server)
    server.add_insecure_port('localhost:50061')  
    server.start()
    print("Buyer notification server started on port 50061")

    _input = input("Press Enter to continue...")

    try:
        
        search_request = buyer_pb2.SearchItemRequest(item_name="", category="ANY")
        search_response = buyer_stub.SearchItem(search_request)
        print("SearchItem Response:")
        print(search_response)

    except grpc.RpcError as e:
        print(f"Error in Buyer Functionality: {e.details()}")

    try:
        
        buy_request = buyer_pb2.BuyItemRequest(
            item_id=1,
            quantity=1,
            buyer_address="localhost:50061"
        )
        buy_response = buyer_stub.BuyItem(buy_request)
        print("BuyItem Response:")
        print(buy_response)

    except grpc.RpcError as e:
        print(f"Error in Buyer Functionality: {e.details()}")

    try:
        
        wishlist_request = buyer_pb2.AddToWishListRequest(
            item_id=3,
            buyer_address="localhost:50061"
        )
        wishlist_response = buyer_stub.AddToWishList(wishlist_request)
        print("AddToWishList Response:")
        print(wishlist_response)

    except grpc.RpcError as e:
        print(f"Error in Buyer Functionality: {e.details()}")

    try:
        
        rate_request = buyer_pb2.RateItemRequest(
            item_id=3,
            buyer_address="localhost:50061",
            rating=4
        )
        rate_response = buyer_stub.RateItem(rate_request)
        print("RateItem Response:")
        print(rate_response)

    except grpc.RpcError as e:
        print(f"Error in Buyer Functionality: {e.details()}")

    finally:
        
        buyer_channel.close()

    server.wait_for_termination()


if __name__ == '__main__':
    run_buyer_instance()
