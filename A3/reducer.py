import grpc
from concurrent import futures
import logging
import sys
import mapReduce_pb2
import mapReduce_pb2_grpc

class Reducer(mapReduce_pb2_grpc.MapReduceServiceServicer):
    def __init__(self):
        # This would typically hold the processed data and other state required by the reducer
        self.data = {}
        self.centroids = []  # List to hold the calculated centroids

    def InitializeReducer(self, request, context):
        # Perform any initialization steps for the reducer
        logging.info(f"Reducer {request.reducerId} initialized")
        return mapReduce_pb2.InitializeReducerResponse(success=True, message="Reducer initialized successfully.")

    def FetchPartitionData(self, request, context):
        # Simulate fetching data for the reducer
        logging.info(f"Fetching data for partition {request.partitionId} from mapper {request.mapperId}")
        # Example response, normally this would be the data from the mapper
        example_data = mapReduce_pb2.KeyValue(key="centroid_id", value="datapoint1,datapoint2")
        return mapReduce_pb2.FetchPartitionResponse(data=[example_data])
    
    def Reduce(self, request, context):
        # This would handle the reduce operation
        key = request.key
        values = request.values
        # Compute new centroid or whatever the reduce operation needs to do
        new_centroid = self.compute_new_centroid(values)
        return mapReduce_pb2.ReduceResponse(new_centroid=new_centroid)
    
    def compute_new_centroid(self, points):
        # Logic to compute new centroid
        pass

    def CompileCentroids(self, request, context):
        # Method to compile centroids and send them back to the master
        logging.info("Compiling centroids")
        if self.centroids:
            return mapReduce_pb2.CompileCentroidsResponse(centroids=self.centroids, success=True)
        else:
            return mapReduce_pb2.CompileCentroidsResponse(success=False, message="No centroids available")

def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mapReduce_pb2_grpc.add_MapReduceServiceServicer_to_server(Reducer(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    logging.info(f"Reducer server started on port {port}")
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    if len(sys.argv) < 2:
        print("Usage: python reducer.py <port>")
        sys.exit(1)
    port = sys.argv[1]
    serve(port)
