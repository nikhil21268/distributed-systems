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

def get_input(prompt, input_type=str):
    while True:
        try:
            user_input = input(prompt)
            return input_type(user_input)
        except ValueError:
            print("Invalid input. Please try again.")

def menu():
    print("Menu:")
    print("1. Register Seller")
    print("2. Sell Item")
    print("3. Update Item")
    print("4. Display Seller Items")
    print("5. Delete Item")
    print("6. Exit")

def run_seller_instance():
    seller_channel = grpc.insecure_channel('34.68.184.144:50053')
    seller_stub = seller_pb2_grpc.SellerServiceStub(seller_channel)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    seller_pb2_grpc.add_SellerServiceServicer_to_server(SellerNotificationServer(), server)
    server.add_insecure_port('localhost:50071')
    server.start()
    print("Seller notification server started on port 50071")

    unique_id = str(uuid.uuid1())

    while True:
        menu()
        choice = get_input("Enter your choice (1-6): ", int)

        if choice == 1:
            try:
                register_request = seller_pb2.RegisterSellerRequest(
                    seller_address="35.226.147.99:50071",
                    seller_uuid=unique_id
                )
                register_response = seller_stub.RegisterSeller(register_request)
                print("RegisterSeller Response:")
                print(register_response)

            except grpc.RpcError as e:
                print(f"Error in Seller Functionality: {e.details()}")

        elif choice == 2:
            try:
                product_name = get_input("Enter product name: ")
                category = get_input("Enter category: ")
                quantity = get_input("Enter quantity: ", int)
                description = get_input("Enter description: ")
                price_per_unit = get_input("Enter price per unit: ", float)
                sell_request = seller_pb2.SellItemRequest(
                    product_name=product_name,
                    category=category,
                    quantity=quantity,
                    description=description,
                    seller_address="35.226.147.99:50071",
                    seller_uuid=unique_id,
                    price_per_unit=price_per_unit
                )
                sell_response = seller_stub.SellItem(sell_request)
                print("SellItem Response:")
                print(sell_response)

            except grpc.RpcError as e:
                print(f"Error in Seller Functionality: {e.details()}")

        elif choice == 3:
            try:
                item_id = get_input("Enter item ID to update: ", int)
                new_price = get_input("Enter new price: ", float)
                new_quantity = get_input("Enter new quantity: ", int)
                update_request = seller_pb2.UpdateItemRequest(
                    item_id=item_id,
                    new_price=new_price,
                    new_quantity=new_quantity,
                    seller_address="35.226.147.99:50071",
                    seller_uuid=unique_id
                )
                update_response = seller_stub.UpdateItem(update_request)
                print("UpdateItem Response:")
                print(update_response)

            except grpc.RpcError as e:
                print(f"Error in Seller Functionality: {e.details()}")

        elif choice == 4:
            try:
                display_request = seller_pb2.DisplaySellerItemsRequest(
                    seller_address="35.226.147.99:50071",
                    seller_uuid=unique_id
                )
                display_response = seller_stub.DisplaySellerItems(display_request)
                print("DisplaySellerItems Response:")
                print(display_response)

            except grpc.RpcError as e:
                print(f"Error in Seller Functionality: {e.details()}")

        elif choice == 5:
            try:
                item_id = get_input("Enter item ID to delete: ", int)
                delete_request = seller_pb2.DeleteItemRequest(
                    item_id=item_id,
                    seller_address="35.226.147.99:50071",
                    seller_uuid=unique_id
                )
                delete_response = seller_stub.DeleteItem(delete_request)
                print("DeleteItem Response:")
                print(delete_response)

            except grpc.RpcError as e:
                print(f"Error in Seller Functionality: {e.details()}")

        elif choice == 6:
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

    seller_channel.close()
    server.wait_for_termination()

if __name__ == '__main__':
    run_seller_instance()
