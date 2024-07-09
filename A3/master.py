import grpc
import mapReduce_pb2
import mapReduce_pb2_grpc
from concurrent import futures
import logging
import random

# Constants for the setup
NUMBER_OF_MAPPERS = 2
NUMBER_OF_REDUCERS = 2
NUMBER_OF_CENTROIDS = 2
NUMBER_OF_ITERATIONS = 2

def load_data_points(filename):
    """
    Load data points from a file where each line contains two numeric values separated by a comma.
    """
    data_points = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 2:
                try:
                    point = (float(parts[0]), float(parts[1]))
                    data_points.append(point)
                except ValueError:
                    print(f"Error converting data {parts} to floats.")
    return data_points

def initialize_centroids(data, k):
    """
    Randomly select k centroids from the dataset and return them as a list of comma-separated strings.
    """
    selected_centroids = random.sample(data, k)
    # Convert each tuple to a string in the format "x,y"
    centroids_as_strings = [f"{centroid[0]},{centroid[1]}" for centroid in selected_centroids]
    return centroids_as_strings

class Master:
    def __init__(self):
        self.data_points = load_data_points("points.txt")
        self.current_centroids = initialize_centroids(self.data_points, NUMBER_OF_CENTROIDS)
        self.mappers = []
        self.reducers = []
        self.mapper_stubs = []
        self.reducer_stubs = []

    def partition_data(self, data_points, num_partitions):
        """
        Splits data into nearly equal parts for distribution to mappers.
        """
        chunk_size = len(data_points) // num_partitions
        remainder = len(data_points) % num_partitions
        partitions = []
        start = 0
        for i in range(num_partitions):
            end = start + chunk_size + (1 if i < remainder else 0)
            partitions.append(data_points[start:end])
            start = end
        return partitions


    def setup_grpc_clients(self):
        # Create gRPC channels and stubs for mappers and reducers
        for i in range(NUMBER_OF_MAPPERS):
            channel = grpc.insecure_channel(f'localhost:{50051+i}')
            self.mapper_stubs.append(mapReduce_pb2_grpc.MapReduceServiceStub(channel))

        for i in range(NUMBER_OF_REDUCERS):
            channel = grpc.insecure_channel(f'localhost:{50151+i}')
            self.reducer_stubs.append(mapReduce_pb2_grpc.MapReduceServiceStub(channel))

    def initialize_mappers(self):
        # Partition the data points among the mappers
        data_partitions = self.partition_data(self.data_points, NUMBER_OF_MAPPERS)
        
        # Initialize all mappers with their chunk of data and current centroids
        for i, (stub, data_chunk) in enumerate(zip(self.mapper_stubs, data_partitions)):
            data_as_strings = [f"{point[0]},{point[1]}" for point in data_chunk]
            request = mapReduce_pb2.InitializeMapperRequest(
                mapperId=i,
                data=data_as_strings,
                centroids=self.current_centroids,
            )
            response = stub.InitializeMapper(request)
            if not response.success:
                logging.error(f"Failed to initialize mapper {i}: {response.message}")

    def initialize_reducers(self):
        # Initialize all reducers
        for i, stub in enumerate(self.reducer_stubs):
            request = mapReduce_pb2.InitializeReducerRequest(reducerId=i)
            response = stub.InitializeReducer(request)
            if not response.success:
                logging.error(f"Failed to initialize reducer {i}: {response.message}")

    def shuffle_and_sort(self, mapped_results):
        from collections import defaultdict
        grouped_results = defaultdict(list)
        for result in mapped_results:
            key, value = result.centroid_index, result.data_point
            grouped_results[key].append(value)
        return grouped_results

    def run_kmeans_iterations(self):
        for iteration in range(NUMBER_OF_ITERATIONS):
            print(f"Running iteration {iteration+1}")
            self.initialize_mappers()
            self.initialize_reducers()

            # Wait for mappers to finish
            input("Press Enter to continue...")
            
            print(self.data_points) 

            # Convert self.data_points to a repeated <class 'mapReduce_pb2.Point'> object
            data_list = [mapReduce_pb2.Point(x=point[0], y=point[1]) for point in self.data_points]

            # Collect results from mappers
            all_mapped_results = []
            for stub in self.mapper_stubs:
                response = stub.Map(mapReduce_pb2.MapRequest(command="map"))
                # Assuming that the Map method is synchronous and returns a collection of results
                all_mapped_results.extend(response.mapped_results)

            print(f"Received {len(all_mapped_results)} mapped results from mappers.")
            print(all_mapped_results)

            # Shuffle and sort the results to group by centroid index
            shuffled_results = self.shuffle_and_sort(all_mapped_results)

            # Send sorted results to the appropriate reducers
            for centroid_index, grouped_data in shuffled_results.items():
                reducer_index = centroid_index % NUMBER_OF_REDUCERS  # Simple partitioning function
                stub = self.reducer_stubs[reducer_index]
                stub.Reduce(mapReduce_pb2.ReduceRequest(data=grouped_data))

            # Collecting outputs from all reducers
            new_centroids = []
            for reducer_stub in self.reducer_stubs:
                try:
                    response = reducer_stub.CompileCentroids(mapReduce_pb2.CompileCentroidsRequest())
                    if response.success:
                        new_centroids.extend(response.centroids)
                    else:
                        print(f"Error retrieving centroids from reducer: {response.message}")
                except grpc.RpcError as e:
                    print(f"RPC failed with {e.code()}: {e.details()}")

            # Assuming new centroids are computed as an average of returned centroids
            # This is a simplification; actual centroid calculation may vary
            if new_centroids:
                # Convert string centroids back to list of lists (assuming format "x,y")
                centroids_list = [list(map(float, centroid.split(','))) for centroid in new_centroids]
                # Calculate the new centroids as the mean of collected centroids
                updated_centroids = []
                if centroids_list:
                    for i in range(len(centroids_list[0])):  # Assuming all centroids have the same dimensions
                        dimension_mean = sum(centroid[i] for centroid in centroids_list) / len(centroids_list)
                        updated_centroids.append(dimension_mean)

                self.current_centroids = updated_centroids
                print(f"Updated centroids for iteration {iteration+1}: {self.current_centroids}")

                # Reinitialize mappers with the new centroids for the next iteration
                self.initialize_mappers_with_new_centroids(self.current_centroids)
            else:
                print("No new centroids received, using previous centroids.")

    def send_to_reducers(self, mapped_results):
        """
        Send the mapped results to the appropriate reducers based on the centroid index.
        Each mapped result contains a (centroid_index, data_point).
        """
        # Assuming self.reducer_stubs is a list of reducer stubs available to the mapper
        # Organize data by reducers

        reducer_data = {}
        for centroid_index, data_point in mapped_results:
            if centroid_index not in reducer_data:
                reducer_data[centroid_index] = []
            reducer_data[centroid_index].append(data_point)

        # Send data to each corresponding reducer
        for centroid_index, data_points in reducer_data.items():
            if centroid_index < len(self.reducer_stubs):  # Check if the reducer index exists
                # Prepare the data for gRPC call
                data_list = [mapReduce_pb2.KeyValue(key=str(centroid_index), value=f"{dp[0]},{dp[1]}") for dp in data_points]
                request = mapReduce_pb2.ProcessDataRequest(data=data_list)
                try:
                    # Assuming ProcessData is the method implemented in reducers to handle incoming data
                    response = self.reducer_stubs[centroid_index].ProcessData(request)
                    if not response.success:
                        print(f"Failed to send data to reducer {centroid_index}: {response.message}")
                except Exception as e:
                    print(f"Error sending data to reducer {centroid_index}: {str(e)}")
            else:
                print(f"No reducer available for centroid index {centroid_index}")

    def start(self):
        self.setup_grpc_clients()
        self.run_kmeans_iterations()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    master = Master()
    master.start()
