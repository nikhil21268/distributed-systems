import grpc
from concurrent import futures
import buyer_pb2
import buyer_pb2_grpc
import seller_pb2
import seller_pb2_grpc
import socket

class BuyerService(buyer_pb2_grpc.BuyerService):
    def __init__(self):
        self.buyers = {}  
        self.wishlists = {}

        self.buyer_notification_channel1 = grpc.insecure_channel('35.224.24.239:50060')
        self.buyer_notification_stub1 = buyer_pb2_grpc.BuyerServiceStub(self.buyer_notification_channel1)

        self.buyer_notification_channel2 = grpc.insecure_channel('35.224.24.239:50061')
        self.buyer_notification_stub2 = buyer_pb2_grpc.BuyerServiceStub(self.buyer_notification_channel2)

        self.seller_channel = grpc.insecure_channel('localhost:50053')
        self.seller_stub = seller_pb2_grpc.SellerServiceStub(self.seller_channel)

    def NotifyItemUpdate(self, request, context):

        
        wishlisted_buyers = []
        if request.id in self.wishlists:
            
            wishlisted_buyers = self.wishlists[request.id]

        
        
        for buyer_adress in wishlisted_buyers:
            buyer_notification = buyer_pb2.ItemNotificationRequest(
                id=request.id,
                price=request.price,
                name=request.name,
                category=request.category,
                description=request.description,  
                quantity_remaining=request.quantity_remaining,
                seller=request.seller,
                rating=request.rating  
            )
            if buyer_adress == "35.224.24.239:50060":
                notification_response = self.buyer_notification_stub1.NotifyItemUpdate(buyer_notification)
                print("NotifyItemUpdate Response:")
                print(notification_response)

            elif buyer_adress == "35.224.24.239:50061":
                notification_response = self.buyer_notification_stub2.NotifyItemUpdate(buyer_notification)

                print("NotifyItemUpdate Response:")
                print(notification_response)

        
        response = buyer_pb2.ItemNotificationResponse(result="SUCCESS")
        return response
    
    def is_port_open(self, ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    
    def get_item_details_from_seller(self, item_id):
        
        
        if True:
            request = seller_pb2.GetItemDetailsRequest(item_id=item_id)
            response = self.seller_stub.GetItemDetails(request)
            return response
        else:
            return None

    def SearchItem(self, request, context):

        item_name = request.item_name
        category = request.category

        print(f"Market prints: Search request for Item name: {item_name}, Category: {category}")

        response = buyer_pb2.SearchItemResponse()

        
        if item_name == "" and category == 'ANY':  
            for item_id in range(1, 10): 
                item_details = self.get_item_details_from_seller(item_id)
                if item_details.id == -1:    
                    continue

                item_response = response.items.add()
                item_response.id = item_details.id
                item_response.price = item_details.price
                item_response.name = item_details.name
                item_response.category = item_details.category
                item_response.description = f"This is {item_details.name}."  
                item_response.quantity_remaining = item_details.quantity_remaining
                item_response.seller = item_details.seller
                item_response.rating = item_details.rating  
        
        elif item_name != "" and category == 'ANY':
            for item_id in range(1, 10): 
                item_details = self.get_item_details_from_seller(item_id)
                if item_details.id == -1:    
                    continue
                if item_details.name == item_name:
                    item_response = response.items.add()
                    item_response.id = item_details.id
                    item_response.price = item_details.price
                    item_response.name = item_details.name
                    item_response.category = item_details.category
                    item_response.description = f"This is {item_details.name}."

        elif item_name == "" and category != 'ANY':
            for item_id in range(1, 10): 
                item_details = self.get_item_details_from_seller(item_id)
                if item_details.id == -1:    
                    continue
                if item_details.category == category:
                    item_response = response.items.add()
                    item_response.id = item_details.id
                    item_response.price = item_details.price
                    item_response.name = item_details.name
                    item_response.category = item_details.category
                    item_response.description = f"This is {item_details.name}."

        elif item_name != "" and category != 'ANY':
            for item_id in range(1, 10): 
                item_details = self.get_item_details_from_seller(item_id)
                if item_details.id == -1:    
                    continue
                if item_details.category == category and item_details.name == item_name:
                    item_response = response.items.add()
                    item_response.id = item_details.id
                    item_response.price = item_details.price
                    item_response.name = item_details.name
                    item_response.category = item_details.category
                    item_response.description = f"This is {item_details.name}."

        return response


    def BuyItem(self, request, context):

        item_id = request.item_id
        quantity = request.quantity
        buyer_address = request.buyer_address

        
        item_details = self.get_item_details_from_seller(item_id)
        if item_details.id == -1:
            response = buyer_pb2.BuyItemResponse(result="FAIL")

        elif item_details.quantity_remaining < quantity:
            response = buyer_pb2.BuyItemResponse(result="FAIL")
        
        else:
            
            item_details.quantity_remaining -= quantity
            response = buyer_pb2.BuyItemResponse(result="SUCCESS")

            print(f"Market prints: Buy request {quantity} of item {item_id}, from {buyer_address}")

            
            seller_notification = seller_pb2.ItemNotificationRequest2(
                id=item_id,
                price=item_details.price,
                name=item_details.name,
                category=item_details.category,
                description=item_details.description,  
                quantity_remaining=item_details.quantity_remaining,
                seller=item_details.seller,
                rating=item_details.rating
            )
            notification_response = self.seller_stub.NotifyItemUpdate2(seller_notification)
            print("NotifyItemUpdate Response:")
            print(notification_response)

            
            update_request = seller_pb2.ItemNotificationRequest2(
                id=item_id,
                quantity_remaining=item_details.quantity_remaining
            )
            update_response = self.seller_stub.UpdateItemDetails(update_request)
            print("UpdateItemDetails Response:")
            print(update_response)

        
        return response

    def AddToWishList(self, request, context):

        item_id = request.item_id
        buyer_address = request.buyer_address

        item_details = self.get_item_details_from_seller(item_id)
        if item_details.id == -1:
            response = buyer_pb2.AddToWishListResponse(result="FAIL")
            return response

        elif item_id not in self.wishlists:
            self.wishlists[item_id] = set()

        self.wishlists[item_id].add(buyer_address)

        response = buyer_pb2.AddToWishListResponse(result="SUCCESS")
        print(f"Market prints: Wishlist request of item {item_id}, from {buyer_address}")

        return response

    def RateItem(self, request, context):
        item_ratings = {}

        item_id = request.item_id
        buyer_address = request.buyer_address
        rating = request.rating

        if item_id not in item_ratings:
            item_ratings[item_id] = {}

        if buyer_address not in item_ratings[item_id]:
            item_ratings[item_id][buyer_address] = rating
            response = buyer_pb2.RateItemResponse(result="SUCCESS")
            print(f"Market prints: {buyer_address} rated item {item_id} with {rating} stars.")

        else:
            response = buyer_pb2.RateItemResponse(result="FAIL")

        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    buyer_pb2_grpc.add_BuyerServiceServicer_to_server(BuyerService(), server)
    server.add_insecure_port('[::]:50054')
    server.start()
    print("Buyer server started on port 50054")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()