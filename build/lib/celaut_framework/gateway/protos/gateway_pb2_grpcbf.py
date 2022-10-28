from celaut_framework.gateway.protos import framework_buffer_pb2, framework_gateway_pb2

# This is part of the transport protocol (slot) data.
StartService_input = {
    1 : framework_gateway_pb2.celaut__pb2.Any.Metadata.HashTag.Hash,
    2 : framework_gateway_pb2.ServiceWithMeta,
    3 : framework_gateway_pb2.HashWithConfig,
    4 : framework_gateway_pb2.ServiceWithConfig
}

StartService_input_partitions = {
    2 : [
            framework_buffer_pb2.Buffer.Head.Partition(index={
                1 : framework_buffer_pb2.Buffer.Head.Partition(),
                2 : framework_buffer_pb2.Buffer.Head.Partition(index={
                    1 : framework_buffer_pb2.Buffer.Head.Partition(index={
                        3 : framework_buffer_pb2.Buffer.Head.Partition(),
                        4 : framework_buffer_pb2.Buffer.Head.Partition(),
                    }),
                    2 : framework_buffer_pb2.Buffer.Head.Partition(),
                    3 : framework_buffer_pb2.Buffer.Head.Partition(),
                    4 : framework_buffer_pb2.Buffer.Head.Partition(),
                })
            }),
            framework_buffer_pb2.Buffer.Head.Partition(index={
                2 : framework_buffer_pb2.Buffer.Head.Partition(index={
                    1 : framework_buffer_pb2.Buffer.Head.Partition(index={
                        1 : framework_buffer_pb2.Buffer.Head.Partition(),
                        2 : framework_buffer_pb2
                        .Buffer.Head.Partition()
                    }),
                })
            })
        ],
    4 : [
            framework_buffer_pb2.Buffer.Head.Partition(index={
                2 : framework_buffer_pb2.Buffer.Head.Partition(index={
                    1 : framework_buffer_pb2.Buffer.Head.Partition(),
                    2 : framework_buffer_pb2.Buffer.Head.Partition(index={
                        1 : framework_buffer_pb2.Buffer.Head.Partition(index={
                            3 : framework_buffer_pb2.Buffer.Head.Partition(),
                            4 : framework_buffer_pb2.Buffer.Head.Partition(),
                        }),
                        2 : framework_buffer_pb2.Buffer.Head.Partition(),
                        3 : framework_buffer_pb2.Buffer.Head.Partition(),
                        4 : framework_buffer_pb2.Buffer.Head.Partition(),
                    })
                }),
                3 : framework_buffer_pb2.Buffer.Head.Partition()
            }),
            framework_buffer_pb2.Buffer.Head.Partition(index={
                2 : framework_buffer_pb2.Buffer.Head.Partition(index={
                    2 : framework_buffer_pb2.Buffer.Head.Partition(index={
                        1 : framework_buffer_pb2.Buffer.Head.Partition(index={
                            1 : framework_buffer_pb2.Buffer.Head.Partition(),
                            2 : framework_buffer_pb2.Buffer.Head.Partition()
                        }),
                    })
                })
            })
        ]
}


"""
    // ( celaut.Any.Metadata.HashTag.Hash=H, celaut.Any=S, celaut.Configuration=C; { H v S v H^C v S^C } )

    // 2. S partition [(1, 2.4, 3, 4), (2.1, 2.2, 2.3)]

    // 3. H^C 
    message HashWithConfig { 
        celaut.Any.Metadata.HashTag.Hash hash = 1;
        celaut.Configuration config = 3;  
    }

    // 4. S^C  partition [(1, 2.4, 3, 4), (2.1, 2.2, 2.3)]
    message ServiceWithConfig { 
        celaut.Any service = 2;
        celaut.Configuration config = 3;
    }
.proto
"""