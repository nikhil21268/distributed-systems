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

def get_input(prompt, input_type=str):
    while True:
        try:
            user_input = input(prompt)
            return input_type(user_input)
        except ValueError:
            print("Invalid input. Please try again.")

def menu():
    print("Menu:")
    print("1. Search for items")
    print("2. Buy an item")
    print("3. Add item to wishlist")
    print("4. Rate an item")
    print("5. Exit")

def run_buyer_instance():
    buyer_channel = grpc.insecure_channel('34.68.184.144:50054')
    buyer_stub = buyer_pb2_grpc.BuyerServiceStub(buyer_channel)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    buyer_pb2_grpc.add_BuyerServiceServicer_to_server(BuyerNotificationServer(), server)
    server.add_insecure_port('localhost:50061')
    server.start()
    print("Buyer notification server started on port 50061")

    while True:
        menu()
        choice = get_input("Enter your choice (1-5): ", int)

        if choice == 1:
            item_name = get_input("Enter item name: ")
            category = get_input("Enter category: ")
            search_request = buyer_pb2.SearchItemRequest(item_name=item_name, category=category)
            search_response = buyer_stub.SearchItem(search_request)
            print("SearchItem Response:")
            print(search_response)

        elif choice == 2:
            item_id = get_input("Enter item ID to buy: ", int)
            quantity = get_input("Enter quantity to buy: ", int)
            buyer_address = "35.224.24.239:50061"
            buy_request = buyer_pb2.BuyItemRequest(
                item_id=item_id,
                quantity=quantity,
                buyer_address=buyer_address
            )
            buy_response = buyer_stub.BuyItem(buy_request)
            print("BuyItem Response:")
            print(buy_response)

        elif choice == 3:
            item_id = get_input("Enter item ID to add to wishlist: ", int)
            wishlist_request = buyer_pb2.AddToWishListRequest(
                item_id=item_id,
                buyer_address=buyer_address
            )
            wishlist_response = buyer_stub.AddToWishList(wishlist_request)
            print("AddToWishList Response:")
            print(wishlist_response)

        elif choice == 4:
            item_id = get_input("Enter item ID to rate: ", int)
            rating = get_input("Enter rating: ", int)
            rate_request = buyer_pb2.RateItemRequest(
                item_id=item_id,
                buyer_address=buyer_address,
                rating=rating
            )
            rate_response = buyer_stub.RateItem(rate_request)
            print("RateItem Response:")
            print(rate_response)

        elif choice == 5:
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

    buyer_channel.close()
    server.wait_for_termination()

if __name__ == '__main__':
    run_buyer_instance()
