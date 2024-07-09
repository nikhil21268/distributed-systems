import grpc
from concurrent import futures
import logging
import sys
import mapReduce_pb2
import mapReduce_pb2_grpc
import numpy as np

class Mapper(mapReduce_pb2_grpc.MapReduceServiceServicer):
    def __init__(self):
        self.centroids = []
        self.data = []
        self.mapper_id = None

    def InitializeMapper(self, request, context):
        self.mapper_id = request.mapperId
        self.data = [tuple(map(float, point.split(','))) for point in request.data]
        self.centroids = [np.array(list(map(float, centroid.split(',')))) for centroid in request.centroids]
        logging.info(f"Mapper {self.mapper_id} initialized with data and centroids.")
        return mapReduce_pb2.InitializeMapperResponse(success=True, message="Mapper initialized successfully.")
    
    def ProcessData(self, data_points, centroids):
        """
        Process the assigned data to find the closest centroid for each point.
        """
        results = []
        for point in data_points:
            min_distance = float('inf')
            closest_centroid = None
            for idx, centroid in enumerate(centroids):
                distance = self.calculate_distance(point, centroid)
                if distance < min_distance:
                    min_distance = distance
                    closest_centroid = idx
            results.append((closest_centroid, point))
        return results

    def calculate_distance(self, point1, point2):
        # Assuming 2D points, extend this for more dimensions
        return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
    
    def Map(self, request, context):        
        # Process data
        mapped_results = self.ProcessData(self.data, self.centroids)
        print("mapped_results", mapped_results)
        print(type(mapped_results))
        return mapReduce_pb2.PointList(success=True, message="Data mapped successfully.")

def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mapReduce_pb2_grpc.add_MapReduceServiceServicer_to_server(Mapper(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    logging.info(f"Mapper server started on port {port}")
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    if len(sys.argv) < 2:
        print("Usage: python mapper.py <port>")
        sys.exit(1)
    port = sys.argv[1]
    serve(port)


'''python mapper.py 50051
python mapper.py 50052
python mapper.py 50053'''