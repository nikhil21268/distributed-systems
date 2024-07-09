import grpc
import seller_pb2
import seller_pb2_grpc
from concurrent import futures
import uuid

class SellerNotificationServer(seller_pb2_grpc.SellerServiceServicer):
    def NotifyItemUpdate2(self, request, context):
        print("Received item update notification:")
        print(f"Item ID: {request.id}, Price: ${request.price}, Name: {request.name}, "
              f"Category: {request.category},")
        print(f"Description: {request.description}, Quantity Remaining: {request.quantity_remaining}")
        print(f"Seller: {request.seller}, Rating: {request.rating}")

        response = seller_pb2.ItemNotificationResponse2(result="SUCCESS")
        return response

def run_seller_instance():
    
    seller_channel = grpc.insecure_channel('localhost:50053')

    
    seller_stub = seller_pb2_grpc.SellerServiceStub(seller_channel)

    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    seller_pb2_grpc.add_SellerServiceServicer_to_server(SellerNotificationServer(), server)
    server.add_insecure_port('localhost:50071') 
    server.start()
    print("Seller notification server started on port 50071")

    unique_id = str(uuid.uuid1())

    try:
        
        register_request = seller_pb2.RegisterSellerRequest(
            seller_address="localhost:50071",
            seller_uuid=unique_id
        )
        register_response = seller_stub.RegisterSeller(register_request)
        print("RegisterSeller Response:")
        print(register_response)

    except grpc.RpcError as e:
        print(f"Error in Seller Functionality: {e.details()}")

    try:
        
        sell_request = seller_pb2.SellItemRequest(
            product_name="Smartphone",
            category="ELECTRONICS",
            quantity=10,
            description="High-quality smartphone",
            seller_address="localhost:50071",
            seller_uuid=unique_id,
            price_per_unit=499.99
        )
        sell_response = seller_stub.SellItem(sell_request)
        print("SellItem Response:")
        print(sell_response)

    except grpc.RpcError as e:
        print(f"Error in Seller Functionality: {e.details()}")

    try:
        
        update_request = seller_pb2.UpdateItemRequest(
            item_id=1,
            new_price=599.99,
            new_quantity=8,
            seller_address="localhost:50071",
            seller_uuid=unique_id
        )
        update_response = seller_stub.UpdateItem(update_request)
        print("UpdateItem Response:")
        print(update_response)

    except grpc.RpcError as e:
        print(f"Error in Seller Functionality: {e.details()}")

    try:
        
        display_request = seller_pb2.DisplaySellerItemsRequest(
            seller_address="localhost:50071",
            seller_uuid=unique_id
        )
        display_response = seller_stub.DisplaySellerItems(display_request)
        print("DisplaySellerItems Response:")
        print(display_response)

    except grpc.RpcError as e:
        print(f"Error in Seller Functionality: {e.details()}")

    
    
    try:
        # DeleteItem
        delete_request = seller_pb2.DeleteItemRequest(
            item_id=1,
            seller_address="localhost:50071",
            seller_uuid="987a515c-a6e5-11ed-906b-76aef1e817c5"
        )
        delete_response = seller_stub.DeleteItem(delete_request)
        print("DeleteItem Response:")
        print(delete_response)

    except grpc.RpcError as e:
        print(f"Error in Seller Functionality: {e.details()}")
    

    

    finally:
        
        seller_channel.close()


    server.wait_for_termination()


if __name__ == '__main__':
    run_seller_instance()
