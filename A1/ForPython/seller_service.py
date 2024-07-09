import grpc
from concurrent import futures
import seller_pb2
import seller_pb2_grpc
import buyer_pb2
import buyer_pb2_grpc


class SellerService(seller_pb2_grpc.SellerService):
    def __init__(self):
        super().__init__()
        self.sellers = {}
        self.items = {}

        # 35.226.147.99
        self.seller_notification_channel1 = grpc.insecure_channel('35.226.147.99:50070')
        self.seller_notification_stub1 = seller_pb2_grpc.SellerServiceStub(self.seller_notification_channel1)

        self.seller_notification_channel2 = grpc.insecure_channel('35.226.147.99:50071')
        self.seller_notification_stub2 = seller_pb2_grpc.SellerServiceStub(self.seller_notification_channel2)

        self.buyer_channel = grpc.insecure_channel('localhost:50054')
        self.buyer_stub = buyer_pb2_grpc.BuyerServiceStub(self.buyer_channel)

    def NotifyItemUpdate2(self, request, context):

        seller_notification = seller_pb2.ItemNotificationRequest2(
            id=request.id,
            price=request.price,
            name=request.name,
            category=request.category,
            description=request.description,
            quantity_remaining=request.quantity_remaining,
            seller=request.seller,
            rating=request.rating
        )

        if request.seller == "35.226.147.99:50070":
            notification_response = self.seller_notification_stub1.NotifyItemUpdate2(seller_notification)
            print("NotifyItemUpdate Response:")
            print(notification_response)

        elif request.seller == "35.226.147.99:50071":
            notification_response = self.seller_notification_stub2.NotifyItemUpdate2(seller_notification)

            print("NotifyItemUpdate Response:")
            print(notification_response)


        response = seller_pb2.ItemNotificationResponse2(result="SUCCESS")
        return response

    def UpdateItemDetails(self, request, context):

        updated_item_id = request.id
        updated_quantity_remaining = request.quantity_remaining


        if updated_item_id in self.items:
            self.items[updated_item_id]["quantity"] = updated_quantity_remaining
            response = seller_pb2.ItemNotificationResponse2(result="SUCCESS")
        else:
            response = seller_pb2.ItemNotificationResponse2(result="FAIL", message=f"Item {updated_item_id} not found")

        return response


    def GetItemDetails(self, request, context):

        item_id = request.item_id

        if item_id not in self.items:

            response = seller_pb2.GetItemDetailsResponse(
                id=-1,
                price=0,
                name="unknown",
                category="unknown",
                description="unknown",
                quantity_remaining=-1,
                seller="unknown",
                rating=0
            )

        else:

            response = seller_pb2.GetItemDetailsResponse(
                id=item_id,
                price=self.items[item_id]["price"],
                name=self.items[item_id]["name"],
                category=self.items[item_id]["category"],
                description=self.items[item_id]["description"],
                quantity_remaining=self.items[item_id]["quantity"],
                seller=self.items[item_id]["seller"],
                rating=self.items[item_id]["rating"]
            )

        try:




            return response
        except Exception as e:

            print(f"Error during serialization: {e}")
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Failed to serialize response!")
            return seller_pb2.GetItemDetailsResponse()

    def RegisterSeller(self, request, context):

        seller_address = request.seller_address
        seller_uuid = request.seller_uuid

        print(f"Market prints: Seller join request from {seller_address}, seller_uuid = {seller_uuid}")

        response = seller_pb2.RegisterSellerResponse()

        if seller_uuid in self.sellers:
            response.result = "FAIL"
        else:
            self.sellers[seller_uuid] = {"seller_address": seller_address}
            response.result = "SUCCESS"

        return response

    def SellItem(self, request, context):

        seller_address = request.seller_address
        seller_uuid = request.seller_uuid

        print(f"Market prints: Sell Item request from {seller_address}")

        response = seller_pb2.SellItemResponse()

        if seller_uuid not in self.sellers:
            response.result = "FAIL"
        else:

            item_id = len(self.items) + 1
            self.items[item_id] = {
                "name": request.product_name,
                "category": request.category,
                "quantity": request.quantity,
                "description": request.description,
                "price": request.price_per_unit,
                "seller": seller_address,
                "rating": 0
            }
            response.result = "SUCCESS"
            response.item_id = item_id

        return response

    def UpdateItem(self, request, context):

        seller_address = request.seller_address
        seller_uuid = request.seller_uuid
        item_id = request.item_id

        print(f"Market prints: Update Item {item_id} request from {seller_address}")

        response = seller_pb2.UpdateItemResponse()

        if seller_uuid not in self.sellers or item_id not in self.items:
            response.result = "FAIL"
        else:

            self.items[item_id]["price"] = request.new_price
            self.items[item_id]["quantity"] = request.new_quantity
            response.result = "SUCCESS"


            buyer_notification = buyer_pb2.ItemNotificationRequest(
                id=item_id,
                price=self.items[item_id]["price"],
                name=self.items[item_id]["name"],
                category=self.items[item_id]["category"],
                description="",
                quantity_remaining=self.items[item_id]["quantity"],
                seller=seller_address,
                rating=0
            )
            notification_response = self.buyer_stub.NotifyItemUpdate(buyer_notification)
            print("NotifyItemUpdate Response:")
            print(notification_response)

        return response

    def DeleteItem(self, request, context):

        seller_address = request.seller_address
        seller_uuid = request.seller_uuid
        item_id = request.item_id

        print(f"Market prints: Delete Item {item_id} request from {seller_address}")

        response = seller_pb2.DeleteItemResponse()

        if seller_uuid not in self.sellers or item_id not in self.items:
            response.result = "FAIL"
        else:

            del self.items[item_id]
            response.result = "SUCCESS"

        return response

    def DisplaySellerItems(self, request, context):

        seller_address = request.seller_address

        print(f"Market prints: Display Items request from {seller_address}")

        response = seller_pb2.DisplaySellerItemsResponse()

        for item_id, item_info in self.items.items():
            if item_info["seller"] == seller_address:
                item_response = response.items.add()
                item_response.id = item_id
                item_response.price = item_info["price"]
                item_response.name = item_info["name"]
                item_response.category = item_info["category"]
                item_response.description = item_info["description"]
                item_response.quantity_remaining = item_info["quantity"]
                item_response.seller = item_info["seller"]
                item_response.rating = item_info["rating"]

        return response

if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    seller_pb2_grpc.add_SellerServiceServicer_to_server(SellerService(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    print("Seller server started on port 50053")
    server.wait_for_termination()
