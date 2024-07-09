package EarlierFiles;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import buyer.BuyerGrpc;
import buyer.BuyerOuterClass;

public class BuyerClient {

    private final ManagedChannel channel;
    private final BuyerGrpc.BuyerBlockingStub stub;

    public BuyerClient(String serverAddress) {
        this.channel = ManagedChannelBuilder.forTarget(serverAddress)
                .usePlaintext()
                .build();
        this.stub = BuyerGrpc.newBlockingStub(channel);
    }

    public void searchItem(String itemName, String category) {
        // Implement logic for SearchItem function
        BuyerOuterClass.SearchItemRequest request = BuyerOuterClass.SearchItemRequest.newBuilder()
                .setItemName(itemName)
                .setCategory(category)
                .build();

        BuyerOuterClass.SearchItemResponse response = stub.searchItem(request);
        System.out.println("Search Item Response:");
        for (BuyerOuterClass.Item item : response.getItemsList()) {
            System.out.printf("Item ID: %d, Price: $%.2f, Name: %s, Category: %s, Description: %s, " +
                            "Quantity Remaining: %d, Rating: %.1f | Seller: %s%n",
                    item.getId(), item.getPrice(), item.getName(), item.getCategory(),
                    item.getDescription(), item.getQuantityRemaining(), item.getRating(),
                    item.getSeller());
        }
    }

    public void buyItem(int itemId, int quantity, String buyerAddress) {
        // Implement logic for BuyItem function
        BuyerOuterClass.BuyItemRequest request = BuyerOuterClass.BuyItemRequest.newBuilder()
                .setItemId(itemId)
                .setQuantity(quantity)
                .setBuyerAddress(buyerAddress)
                .build();

        BuyerOuterClass.BuyItemResponse response = stub.buyItem(request);
        System.out.println("Buy Item Response: " + response.getResult());
        // Process the response as needed
    }

    public void addToWishList(int itemId, String buyerAddress) {
        // Implement logic for AddToWishList function
        BuyerOuterClass.AddToWishListRequest request = BuyerOuterClass.AddToWishListRequest.newBuilder()
                .setItemId(itemId)
                .setBuyerAddress(buyerAddress)
                .build();

        BuyerOuterClass.AddToWishListResponse response = stub.addToWishList(request);
        System.out.println("Add to Wishlist Response: " + response.getResult());
        // Process the response as needed
    }

    public void rateItem(int itemId, String buyerAddress, int rating) {
        // Implement logic for RateItem function
        BuyerOuterClass.RateItemRequest request = BuyerOuterClass.RateItemRequest.newBuilder()
                .setItemId(itemId)
                .setBuyerAddress(buyerAddress)
                .setRating(rating)
                .build();

        BuyerOuterClass.RateItemResponse response = stub.rateItem(request);
        System.out.println("Rate Item Response: " + response.getResult());
        // Process the response as needed
    }

    public void notifyClient(String notificationMessage) {
        // Implement logic for NotifyClient function
        System.out.println("Notification received: " + notificationMessage);
    }

    // Implement other functions for additional buyer-related actions

    public void shutdown() {
        channel.shutdown();
    }

    public static void main(String[] args) {
        BuyerClient buyerClient = new BuyerClient("localhost:50051");  // Replace with the actual Market server address
        buyerClient.searchItem("iPhone", "ELECTRONICS");
        // Call other functions as needed based on the assignment requirements
        buyerClient.shutdown();
    }
}
