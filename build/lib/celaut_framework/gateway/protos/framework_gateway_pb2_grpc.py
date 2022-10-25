# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from celaut_framework.gateway.protos import framework_buffer_pb2 as framework__buffer__pb2


class GatewayStub(object):
    """GRPC.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartService = channel.stream_stream(
                '/framework_gateway.Gateway/StartService',
                request_serializer=framework__buffer__pb2.Buffer.SerializeToString,
                response_deserializer=framework__buffer__pb2.Buffer.FromString,
                )
        self.StopService = channel.stream_stream(
                '/framework_gateway.Gateway/StopService',
                request_serializer=framework__buffer__pb2.Buffer.SerializeToString,
                response_deserializer=framework__buffer__pb2.Buffer.FromString,
                )
        self.ModifyServiceSystemResources = channel.stream_stream(
                '/framework_gateway.Gateway/ModifyServiceSystemResources',
                request_serializer=framework__buffer__pb2.Buffer.SerializeToString,
                response_deserializer=framework__buffer__pb2.Buffer.FromString,
                )


class GatewayServicer(object):
    """GRPC.
    """

    def StartService(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopService(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ModifyServiceSystemResources(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GatewayServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartService': grpc.stream_stream_rpc_method_handler(
                    servicer.StartService,
                    request_deserializer=framework__buffer__pb2.Buffer.FromString,
                    response_serializer=framework__buffer__pb2.Buffer.SerializeToString,
            ),
            'StopService': grpc.stream_stream_rpc_method_handler(
                    servicer.StopService,
                    request_deserializer=framework__buffer__pb2.Buffer.FromString,
                    response_serializer=framework__buffer__pb2.Buffer.SerializeToString,
            ),
            'ModifyServiceSystemResources': grpc.stream_stream_rpc_method_handler(
                    servicer.ModifyServiceSystemResources,
                    request_deserializer=framework__buffer__pb2.Buffer.FromString,
                    response_serializer=framework__buffer__pb2.Buffer.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'framework_gateway.Gateway', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Gateway(object):
    """GRPC.
    """

    @staticmethod
    def StartService(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/framework_gateway.Gateway/StartService',
            framework__buffer__pb2.Buffer.SerializeToString,
            framework__buffer__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopService(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/framework_gateway.Gateway/StopService',
            framework__buffer__pb2.Buffer.SerializeToString,
            framework__buffer__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ModifyServiceSystemResources(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/framework_gateway.Gateway/ModifyServiceSystemResources',
            framework__buffer__pb2.Buffer.SerializeToString,
            framework__buffer__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
