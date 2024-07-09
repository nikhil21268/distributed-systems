# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import market_pb2 as market__pb2


class MarketServiceStub(object):
    """gRPC service definition
    ... (other RPC methods)
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.NotifyClient = channel.unary_unary(
                '/market.MarketService/NotifyClient',
                request_serializer=market__pb2.NotifyClientNotification.SerializeToString,
                response_deserializer=market__pb2.NotifyClientResponse.FromString,
                )


class MarketServiceServicer(object):
    """gRPC service definition
    ... (other RPC methods)
    """

    def NotifyClient(self, request, context):
        """RPC method for notifying clients (buyers/sellers)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MarketServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'NotifyClient': grpc.unary_unary_rpc_method_handler(
                    servicer.NotifyClient,
                    request_deserializer=market__pb2.NotifyClientNotification.FromString,
                    response_serializer=market__pb2.NotifyClientResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'market.MarketService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MarketService(object):
    """gRPC service definition
    ... (other RPC methods)
    """

    @staticmethod
    def NotifyClient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/market.MarketService/NotifyClient',
            market__pb2.NotifyClientNotification.SerializeToString,
            market__pb2.NotifyClientResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
