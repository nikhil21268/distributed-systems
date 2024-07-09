import grpc
import buyer_pb2
import buyer_pb2_grpc
import seller_pb2
import seller_pb2_grpc
import market_pb2
import market_pb2_grpc

def run_client():
    # Create gRPC channels
    buyer_channel = grpc.insecure_channel('localhost:50054')
    seller_channel = grpc.insecure_channel('localhost:50053')
    market_channel = grpc.insecure_channel('localhost:50052')

    # Create stubs
    buyer_stub = buyer_pb2_grpc.BuyerServiceStub(buyer_channel)
    seller_stub = seller_pb2_grpc.SellerServiceStub(seller_channel)
    market_stub = market_pb2_grpc.MarketServiceStub(market_channel)
        
    try:
        
        # RegisterSeller
        register_request = seller_pb2.RegisterSellerRequest(
            seller_address="localhost:50053",
            seller_uuid="987a515c-a6e5-11ed-906b-76aef1e817c5"
        )
        register_response = seller_stub.RegisterSeller(register_request)
        print("RegisterSeller Response:")
        print(register_response)

    except grpc.RpcError as e:
        print(f"Error in Seller Functionality: {e.details()}")

    try:
        
        # SellItem
        sell_request = seller_pb2.SellItemRequest(
            product_name="Smartphone",
            category="ELECTRONICS",
            quantity=10,
            description="High-quality smartphone",
            seller_address="localhost:50053",
            seller_uuid="987a515c-a6e5-11ed-906b-76aef1e817c5",
            price_per_unit=499.99
        )
        sell_response = seller_stub.SellItem(sell_request)
        print("SellItem Response:")
        print(sell_response)

    except grpc.RpcError as e:
        print(f"Error in Seller Functionality: {e.details()}")

    try:
        
        # UpdateItem
        update_request = seller_pb2.UpdateItemRequest(
            item_id=1,
            new_price=599.99,
            new_quantity=8,
            seller_address="localhost:50053",
            seller_uuid="987a515c-a6e5-11ed-906b-76aef1e817c5"
        )
        update_response = seller_stub.UpdateItem(update_request)
        print("UpdateItem Response:")
        print(update_response)
        

    except grpc.RpcError as e:
        print(f"Error in Seller Functionality: {e.details()}")

    
    try:
        
        # DeleteItem
        delete_request = seller_pb2.DeleteItemRequest(
            item_id=1,
            seller_address="localhost:50053",
            seller_uuid="987a515c-a6e5-11ed-906b-76aef1e817c5"
        )
        delete_response = seller_stub.DeleteItem(delete_request)
        print("DeleteItem Response:")
        print(delete_response)

    except grpc.RpcError as e:
        print(f"Error in Seller Functionality: {e.details()}")


    try:
        
        # DisplaySellerItems
        display_request = seller_pb2.DisplaySellerItemsRequest(
            seller_address="192.13.188.178:50051",
            seller_uuid="987a515c-a6e5-11ed-906b-76aef1e817c5"
        )
        display_response = seller_stub.DisplaySellerItems(display_request)
        print("DisplaySellerItems Response:")
        print(display_response)

    except grpc.RpcError as e:
        print(f"Error in Seller Functionality: {e.details()}")

    
    try:
        
        # SearchItem
        search_request = buyer_pb2.SearchItemRequest(item_name="", category="ANY")
        search_response = buyer_stub.SearchItem(search_request)
        print("SearchItem Response:")
        print(search_response)

    except grpc.RpcError as e:
        print(f"Error in Seller Functionality: {e.details()}")


    try:
        
        # BuyItem
        buy_request = buyer_pb2.BuyItemRequest(
            item_id=1,
            quantity=1,
            buyer_address="localhost:50054"
        )
        buy_response = buyer_stub.BuyItem(buy_request)
        print("BuyItem Response:")
        print(buy_response)

    except grpc.RpcError as e:
        print(f"Error in Seller Functionality: {e.details()}")

    try:
        
        # AddToWishList
        wishlist_request = buyer_pb2.AddToWishListRequest(
            item_id=3,
            buyer_address="localhost:50054"
        )
        wishlist_response = buyer_stub.AddToWishList(wishlist_request)
        print("AddToWishList Response:")
        print(wishlist_response)

    except grpc.RpcError as e:
        print(f"Error in Seller Functionality: {e.details()}")

    try:
        
        # RateItem
        rate_request = buyer_pb2.RateItemRequest(
            item_id=3,
            buyer_address="localhost:50054",
            rating=4
        )
        rate_response = buyer_stub.RateItem(rate_request)
        print("RateItem Response:")
        print(rate_response)

    except grpc.RpcError as e:
        print(f"Error in Seller Functionality: {e.details()}")

    try:
        
        # NotifyClient (Buyer)
        notify_request_buyer = market_pb2.NotifyClientNotification(
            updated_item=market_pb2.NotifyClientNotification.Item(
                id=1,
                price=599.99,
                name="iPhone",
                category="ELECTRONICS",
                description="This is iPhone 15.",
                quantity_remaining=8,
                seller="localhost:50053",
                rating=4.3
            )
        )
        notify_response_buyer = market_stub.NotifyClient(notify_request_buyer)
        print("NotifyClient Response (Buyer):")
        print(notify_response_buyer)

    except grpc.RpcError as e:
        print(f"Error in Seller Functionality: {e.details()}")

    


    try:
        # Example: Invoke the SearchItem RPC from the buyer service
        search_request = buyer_pb2.SearchItemRequest(item_name="Laptop", category="ELECTRONICS")
        search_response = buyer_stub.SearchItem(search_request)
        print("SearchItem Response:")
        print(search_response)

        # You can add more RPC invocations here for testing other functionalities

    except grpc.RpcError as e:
        print(f"Error: {e.details()}")

    


    
    

    

    try:
        
        # Example: Invoke the NotifyClient RPC from the market service
        notify_request = market_pb2.NotifyClientNotification(
            updated_item=market_pb2.NotifyClientNotification.Item(
                id=1,
                price=499.99,
                name="Smartphone",
                category="ELECTRONICS",
                description="High-quality smartphone",
                quantity_remaining=10,
                seller="123 Main St",
                rating=4.5
            )
        )
        notify_response = market_stub.NotifyClient(notify_request)
        print("NotifyClient Response:")
        print(notify_response)

    except grpc.RpcError as e:
        print(f"Error in Market Functionality: {e.details()}")

    
    finally:
        # Close the channels when done
        seller_channel.close()
        market_channel.close()
        buyer_channel.close()


if __name__ == '__main__':
    run_client()
































# try:
        
    #     # NotifyClient (Seller)
    #     notify_request_seller = market_pb2.NotifyClientNotification(
    #         updated_item=market_pb2.NotifyClientNotification.Item(
    #             id=1,
    #             price=599.99,
    #             name="iPhone",
    #             category="ELECTRONICS",
    #             description="This is iPhone 15.",
    #             quantity_remaining=8,
    #             seller="localhost:50053",
    #             rating=4.3
    #         )
    #     )

    #     # Assuming market_stub is your gRPC stub
    #     response = market_stub.NotifyClient(notify_request_seller)
    #     print(f"NotifyClient Response: {response.result}")

    # except grpc.RpcError as e:
    #     print(f"Error in Seller Functionality: {e.details()}")




# Latest edit ends

    # try:
        
    #     # Example: Invoke the SellItem RPC from the seller service
    #     sell_request = seller_pb2.SellItemRequest(
    #         product_name="Smartphone",
    #         category="ELECTRONICS",
    #         quantity=10,
    #         description="High-quality smartphone",
    #         seller_address="123 Main St",
    #         seller_uuid="seller-123",
    #         price_per_unit=499.99
    #     )
    #     sell_response = seller_stub.SellItem(sell_request)
    #     print("SellItem Response:")
    #     print(sell_response)

    # except grpc.RpcError as e:
    #     print(f"Error in Seller Functionality: {e.details()}")