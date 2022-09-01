def modify_resources_grpcbb(i: dict) -> api_pb2.celaut__pb2.Sysresources:
    return next(
        client_grpc(
            method = gateway_pb2_grpc.GatewayStub(
                        grpc.insecure_channel(ENVS['GATEWAY_MAIN_DIR'])
                    ).ModifyServiceSystemResources,
            input = gateway_pb2.ModifyServiceSystemResourcesInput(
                min_sysreq = celaut_pb2.Sysresources(
                    mem_limit = i['min']
                ),
                max_sysreq = celaut_pb2.Sysresources(
                    mem_limit = i['max']
                ),
            ),
            partitions_message_mode_parser=True,
            indices_parser = api_pb2.celaut__pb2.Sysresources,
        )
    )