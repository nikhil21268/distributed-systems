package EarlierFiles;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import seller.SellerGrpc;
import seller.SellerOuterClass;

public class SellerClient {

    private final ManagedChannel channel;
    private final SellerGrpc.SellerBlockingStub stub;

    public SellerClient(String serverAddress) {
        this.channel = ManagedChannelBuilder.forTarget(serverAddress)
                .usePlaintext()
                .build();
        this.stub = SellerGrpc.newBlockingStub(channel);
    }

    public void registerSeller(String sellerAddress, String uuid) {
        // Implement logic for RegisterSeller function
        SellerOuterClass.RegisterSellerRequest request = SellerOuterClass.RegisterSellerRequest.newBuilder()
                .setSellerAddress(sellerAddress)
                .setUuid(uuid)
                .build();

        SellerOuterClass.RegisterSellerResponse response = stub.registerSeller(request);
        System.out.println("Register Seller Response: " + response.getResult());
        // Process the response as needed
    }

    public void sellItem(SellerOuterClass.SellItemRequest itemDetails) {
        // Implement logic for SellItem function
        SellerOuterClass.SellItemResponse response = stub.sellItem(itemDetails);
        System.out.println("Sell Item Response: " + response.getResult());
        // Process the response as needed
    }

    public void updateItem(int itemId, double newPrice, int newQuantity) {
        // Implement logic for UpdateItem function
        SellerOuterClass.UpdateItemRequest request = SellerOuterClass.UpdateItemRequest.newBuilder()
                .setItemId(itemId)
                .setNewPrice(newPrice)
                .setNewQuantity(newQuantity)
                .build();

        SellerOuterClass.UpdateItemResponse response = stub.updateItem(request);
        System.out.println("Update Item Response: " + response.getResult());
        // Process the response as needed
    }

    public void deleteItem(int itemId) {
        // Implement logic for DeleteItem function
        SellerOuterClass.DeleteItemRequest request = SellerOuterClass.DeleteItemRequest.newBuilder()
                .setItemId(itemId)
                .build();

        SellerOuterClass.DeleteItemResponse response = stub.deleteItem(request);
        System.out.println("Delete Item Response: " + response.getResult());
        // Process the response as needed
    }

    public void displaySellerItems(String sellerAddress, String uuid) {
        // Implement logic for DisplaySellerItems function
        SellerOuterClass.DisplaySellerItemsRequest request = SellerOuterClass.DisplaySellerItemsRequest.newBuilder()
                .setSellerAddress(sellerAddress)
                .setUuid(uuid)
                .build();

        SellerOuterClass.DisplaySellerItemsResponse response = stub.displaySellerItems(request);
        System.out.println("Display Seller Items Response:");
        for (SellerOuterClass.Item item : response.getItemsList()) {
            System.out.printf("Item ID: %d, Price: $%.2f, Name: %s, Category: %s, Description: %s, " +
                            "Quantity Remaining: %d, Seller: %s, Rating: %.1f%n",
                    item.getId(), item.getPrice(), item.getName(), item.getCategory(),
                    item.getDescription(), item.getQuantityRemaining(), item.getSeller(),
                    item.getRating());
        }
    }

    // Implement other functions for additional seller-related actions

    public void shutdown() {
        channel.shutdown();
    }

    public static void main(String[] args) {
        SellerClient sellerClient = new SellerClient("localhost:50051");  // Replace with the actual Market server address
        sellerClient.registerSeller("192.13.188.178:50051", "987a515c-a6e5-11ed-906b-76aef1e817c5");
        // Call other functions as needed based on the assignment requirements
        sellerClient.shutdown();
    }
}
