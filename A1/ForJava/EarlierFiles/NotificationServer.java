package EarlierFiles;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.stub.StreamObserver;
import notification.NotificationGrpc;
import notification.NotificationOuterClass;

public class NotificationServer extends NotificationGrpc.NotificationImplBase {

    @Override
    public void notifyClient(NotificationOuterClass.NotifyClientRequest request,
                             StreamObserver<NotificationOuterClass.NotifyClientResponse> responseObserver) {
        // Implement logic for handling notifications
        System.out.println("#######");
        System.out.println("The Following Item has been updated:");
        System.out.printf("Item ID: %d, Price: $%.2f, Name: %s, Category: %s, Description: %s, " +
                        "Quantity Remaining: %d, Rating: %.1f | Seller: %s%n",
                request.getItem().getId(), request.getItem().getPrice(), request.getItem().getName(),
                request.getItem().getCategory(), request.getItem().getDescription(),
                request.getItem().getQuantityRemaining(), request.getItem().getRating(),
                request.getItem().getSeller());
        System.out.println("#######");
        // Process the notification as needed

        // Send the response to the client
        NotificationOuterClass.NotifyClientResponse response = NotificationOuterClass.NotifyClientResponse.newBuilder()
                .setResult("Notification received")
                .build();
        responseObserver.onNext(response);
        responseObserver.onCompleted();
    }

    public static void main(String[] args) throws Exception {
        NotificationServer notificationServer = new NotificationServer();
        Server server = ServerBuilder.forPort(50052)  // You can use a different port for the notification server
                .addService(notificationServer)
                .build();
        server.start();
        System.out.println("Notification server started on port 50052");
        server.awaitTermination();
    }
}
