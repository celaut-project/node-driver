from celaut_framework.gateway.protos import gateway_pb2
from grpcbigbuffer import buffer_pb2

StartService_input = {
    5 : gateway_pb2.Client,
    6 : gateway_pb2.RecursionGuard,

    1 : gateway_pb2.celaut__pb2.Any.Metadata.HashTag.Hash,
    2 : gateway_pb2.ServiceWithMeta,
    3 : gateway_pb2.HashWithConfig,
    4 : gateway_pb2.ServiceWithConfig
}

StartService_input_partitions = {
    2 : [
            buffer_pb2.Buffer.Head.Partition(index={
                1 : buffer_pb2.Buffer.Head.Partition(),
                2 : buffer_pb2.Buffer.Head.Partition(index={
                    1 : buffer_pb2.Buffer.Head.Partition(index={
                        3 : buffer_pb2.Buffer.Head.Partition(),
                        4 : buffer_pb2.Buffer.Head.Partition(),
                    }),
                    2 : buffer_pb2.Buffer.Head.Partition(),
                    3 : buffer_pb2.Buffer.Head.Partition(),
                    4 : buffer_pb2.Buffer.Head.Partition(),
                })
            }),
            buffer_pb2.Buffer.Head.Partition(index={
                2 : buffer_pb2.Buffer.Head.Partition(index={
                    1 : buffer_pb2.Buffer.Head.Partition(index={
                        1 : buffer_pb2.Buffer.Head.Partition(),
                        2 : buffer_pb2.Buffer.Head.Partition()
                    }),
                })
            })
        ],
    4 : [
            buffer_pb2.Buffer.Head.Partition(index={
                2 : buffer_pb2.Buffer.Head.Partition(index={
                    1 : buffer_pb2.Buffer.Head.Partition(),
                    2 : buffer_pb2.Buffer.Head.Partition(index={
                        1 : buffer_pb2.Buffer.Head.Partition(index={
                            3 : buffer_pb2.Buffer.Head.Partition(),
                            4 : buffer_pb2.Buffer.Head.Partition(),
                        }),
                        2 : buffer_pb2.Buffer.Head.Partition(),
                        3 : buffer_pb2.Buffer.Head.Partition(),
                        4 : buffer_pb2.Buffer.Head.Partition(),
                    })
                }),
                3 : buffer_pb2.Buffer.Head.Partition(),
                4 : buffer_pb2.Buffer.Head.Partition(),
                5 : buffer_pb2.Buffer.Head.Partition(),
                6 : buffer_pb2.Buffer.Head.Partition(),
            }),
            buffer_pb2.Buffer.Head.Partition(index={
                2 : buffer_pb2.Buffer.Head.Partition(index={
                    2 : buffer_pb2.Buffer.Head.Partition(index={
                        1 : buffer_pb2.Buffer.Head.Partition(index={
                            1 : buffer_pb2.Buffer.Head.Partition(),
                            2 : buffer_pb2.Buffer.Head.Partition()
                        }),
                    })
                })
            })
        ]
}

StartService_input_single_partition = {
    4: [
            buffer_pb2.Buffer.Head.Partition(index={
                3 : buffer_pb2.Buffer.Head.Partition(),
                4 : buffer_pb2.Buffer.Head.Partition(),
                5 : buffer_pb2.Buffer.Head.Partition(),
                6 : buffer_pb2.Buffer.Head.Partition(),
            }),
           buffer_pb2.Buffer.Head.Partition(index={
                2 : buffer_pb2.Buffer.Head.Partition()
            })
    ]
}