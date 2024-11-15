# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mapReduce_pb2 as mapReduce__pb2


class MapReduceServiceStub(object):
    """The gRPC service definition for MapReduce operations
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.InitializeMapper = channel.unary_unary(
                '/MapReduceService/InitializeMapper',
                request_serializer=mapReduce__pb2.InitializeMapperRequest.SerializeToString,
                response_deserializer=mapReduce__pb2.InitializeMapperResponse.FromString,
                )
        self.Map = channel.unary_unary(
                '/MapReduceService/Map',
                request_serializer=mapReduce__pb2.MapRequest.SerializeToString,
                response_deserializer=mapReduce__pb2.MapResponse.FromString,
                )
        self.InitializeReducer = channel.unary_unary(
                '/MapReduceService/InitializeReducer',
                request_serializer=mapReduce__pb2.InitializeReducerRequest.SerializeToString,
                response_deserializer=mapReduce__pb2.InitializeReducerResponse.FromString,
                )
        self.FetchPartitionData = channel.unary_unary(
                '/MapReduceService/FetchPartitionData',
                request_serializer=mapReduce__pb2.FetchPartitionRequest.SerializeToString,
                response_deserializer=mapReduce__pb2.FetchPartitionResponse.FromString,
                )
        self.CompileCentroids = channel.unary_unary(
                '/MapReduceService/CompileCentroids',
                request_serializer=mapReduce__pb2.CompileCentroidsRequest.SerializeToString,
                response_deserializer=mapReduce__pb2.CompileCentroidsResponse.FromString,
                )


class MapReduceServiceServicer(object):
    """The gRPC service definition for MapReduce operations
    """

    def InitializeMapper(self, request, context):
        """Master to Mapper communication
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Map(self, request, context):
        """Mapper to Mapper communication for fetching mapped_results
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitializeReducer(self, request, context):
        """Master to Reducer communication
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchPartitionData(self, request, context):
        """Reducer to Mapper communication for fetching partitioned data
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CompileCentroids(self, request, context):
        """Master to all Reducers to compile centroids
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MapReduceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'InitializeMapper': grpc.unary_unary_rpc_method_handler(
                    servicer.InitializeMapper,
                    request_deserializer=mapReduce__pb2.InitializeMapperRequest.FromString,
                    response_serializer=mapReduce__pb2.InitializeMapperResponse.SerializeToString,
            ),
            'Map': grpc.unary_unary_rpc_method_handler(
                    servicer.Map,
                    request_deserializer=mapReduce__pb2.MapRequest.FromString,
                    response_serializer=mapReduce__pb2.MapResponse.SerializeToString,
            ),
            'InitializeReducer': grpc.unary_unary_rpc_method_handler(
                    servicer.InitializeReducer,
                    request_deserializer=mapReduce__pb2.InitializeReducerRequest.FromString,
                    response_serializer=mapReduce__pb2.InitializeReducerResponse.SerializeToString,
            ),
            'FetchPartitionData': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchPartitionData,
                    request_deserializer=mapReduce__pb2.FetchPartitionRequest.FromString,
                    response_serializer=mapReduce__pb2.FetchPartitionResponse.SerializeToString,
            ),
            'CompileCentroids': grpc.unary_unary_rpc_method_handler(
                    servicer.CompileCentroids,
                    request_deserializer=mapReduce__pb2.CompileCentroidsRequest.FromString,
                    response_serializer=mapReduce__pb2.CompileCentroidsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MapReduceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MapReduceService(object):
    """The gRPC service definition for MapReduce operations
    """

    @staticmethod
    def InitializeMapper(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MapReduceService/InitializeMapper',
            mapReduce__pb2.InitializeMapperRequest.SerializeToString,
            mapReduce__pb2.InitializeMapperResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Map(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MapReduceService/Map',
            mapReduce__pb2.MapRequest.SerializeToString,
            mapReduce__pb2.MapResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InitializeReducer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MapReduceService/InitializeReducer',
            mapReduce__pb2.InitializeReducerRequest.SerializeToString,
            mapReduce__pb2.InitializeReducerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FetchPartitionData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MapReduceService/FetchPartitionData',
            mapReduce__pb2.FetchPartitionRequest.SerializeToString,
            mapReduce__pb2.FetchPartitionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CompileCentroids(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MapReduceService/CompileCentroids',
            mapReduce__pb2.CompileCentroidsRequest.SerializeToString,
            mapReduce__pb2.CompileCentroidsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
