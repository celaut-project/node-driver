from celaut_framework.gateway.protos import gateway_pb2

StartService_input = {
    5: gateway_pb2.Client,
    6: gateway_pb2.RecursionGuard,

    1: gateway_pb2.celaut__pb2.Any.Metadata.HashTag.Hash,
    2: gateway_pb2.ServiceWithMeta,
    3: gateway_pb2.HashWithConfig,
    4: gateway_pb2.ServiceWithConfig
}
