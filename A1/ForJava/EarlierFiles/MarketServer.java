package EarlierFiles;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.stub.StreamObserver;
import market.MarketGrpc;
import market.MarketOuterClass;

import java.io.IOException;

public class MarketServer extends MarketGrpc.MarketImplBase {

    @Override
    public void registerSeller(MarketOuterClass.RegisterSellerRequest request,
                               StreamObserver<MarketOuterClass.RegisterSellerResponse> responseObserver) {
        // Implement logic for RegisterSeller
        // Validate seller address and UUID
        // Add seller to the market's records
        // Respond with success or failure
        System.out.println("Seller join request from " + request.getSellerAddress() +
                ", uuid = " + request.getUuid());
        responseObserver.onNext(MarketOuterClass.RegisterSellerResponse.newBuilder()
                .setResult("SUCCESS")
                .build());
        responseObserver.onCompleted();
    }

    @Override
    public void sellItem(MarketOuterClass.SellItemRequest request,
                         StreamObserver<MarketOuterClass.SellItemResponse> responseObserver) {
        // Implement logic for SellItem
        // Process the request, assign a unique item ID, and store buyer ratings
        // Respond with success or failure
        System.out.println("Sell Item request from " + request.getSellerAddress());
        responseObserver.onNext(MarketOuterClass.SellItemResponse.newBuilder()
                .setResult("SUCCESS")
                .build());
        responseObserver.onCompleted();
    }

    @Override
    public void updateItem(MarketOuterClass.UpdateItemRequest request,
                           StreamObserver<MarketOuterClass.UpdateItemResponse> responseObserver) {
        // Implement logic for UpdateItem
        // Validate seller credentials, check if item exists, and update details
        // Trigger notifications to wish-listed buyers
        // Respond with success or failure
        System.out.println("Update Item " + request.getItemId() +
                " request from " + request.getSellerAddress());
        responseObserver.onNext(MarketOuterClass.UpdateItemResponse.newBuilder()
                .setResult("SUCCESS")
                .build());
        responseObserver.onCompleted();
    }

    @Override
    public void deleteItem(MarketOuterClass.DeleteItemRequest request,
                           StreamObserver<MarketOuterClass.DeleteItemResponse> responseObserver) {
        // Implement logic for DeleteItem
        // Validate seller credentials and delete the specified item
        // Respond with success or failure
        System.out.println("Delete Item " + request.getItemId() +
                " request from " + request.getSellerAddress());
        responseObserver.onNext(MarketOuterClass.DeleteItemResponse.newBuilder()
                .setResult("SUCCESS")
                .build());
        responseObserver.onCompleted();
    }

    @Override
    public void displaySellerItems(MarketOuterClass.DisplaySellerItemsRequest request,
                                   StreamObserver<MarketOuterClass.DisplaySellerItemsResponse> responseObserver) {
        // Implement logic for DisplaySellerItems
        // Retrieve and return the list of uploaded items for the seller
        System.out.println("Display Items request from " + request.getSellerAddress());
        // Create and return a response with the list of items
        MarketOuterClass.DisplaySellerItemsResponse response =
                MarketOuterClass.DisplaySellerItemsResponse.newBuilder()
                        .addItems(MarketOuterClass.Item.newBuilder()
                                .setId(1)
                                .setPrice(500)
                                .setName("iPhone")
                                .setCategory("Electronics")
                                .setDescription("This is iPhone 15.")
                                .setQuantityRemaining(5)
                                .setSeller(request.getSellerAddress())
                                .setRating(4.3)
                                .build())
                        // Add more items as needed
                        .build();
        responseObserver.onNext(response);
        responseObserver.onCompleted();
    }

    // Implement other service methods (SearchItem, BuyItem, AddToWishList, RateItem, NotifyClient, etc.)

    public static void main(String[] args) throws IOException, InterruptedException {
        Server server = ServerBuilder.forPort(50051)
                .addService(new MarketServer())
                .build();

        server.start();
        System.out.println("Market server started on port 50051");
        server.awaitTermination();
    }
}
