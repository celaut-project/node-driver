# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: celaut.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63\x65laut.proto\x12\x06\x63\x65laut\"\xe5\x04\n\x08\x46ieldDef\x12.\n\x07message\x18\x01 \x01(\x0b\x32\x1b.celaut.FieldDef.MessageDefH\x00\x12\x32\n\tprimitive\x18\x02 \x01(\x0b\x32\x1d.celaut.FieldDef.PrimitiveDefH\x00\x12(\n\x04\x65num\x18\x03 \x01(\x0b\x32\x18.celaut.FieldDef.EnumDefH\x00\x1a,\n\x0cPrimitiveDef\x12\x12\n\x05regex\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_regex\x1ak\n\x07\x45numDef\x12\x32\n\x05value\x18\x01 \x03(\x0b\x32#.celaut.FieldDef.EnumDef.ValueEntry\x1a,\n\nValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\xa6\x02\n\nMessageDef\x12\x35\n\x05param\x18\x01 \x03(\x0b\x32&.celaut.FieldDef.MessageDef.ParamEntry\x12\x33\n\x05oneof\x18\x02 \x03(\x0b\x32$.celaut.FieldDef.MessageDef.OneofDef\x1a=\n\x08ParamDef\x12\x1f\n\x05\x66ield\x18\x01 \x01(\x0b\x32\x10.celaut.FieldDef\x12\x10\n\x08repeated\x18\x02 \x01(\x08\x1a\x19\n\x08OneofDef\x12\r\n\x05index\x18\x01 \x03(\x05\x1aR\n\nParamEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.celaut.FieldDef.MessageDef.ParamDef:\x02\x38\x01\x42\x07\n\x05value\"\xc5\x03\n\x03\x41ny\x12+\n\x08metadata\x18\x01 \x01(\x0b\x32\x14.celaut.Any.MetadataH\x00\x88\x01\x01\x12\r\n\x05value\x18\x02 \x01(\x0c\x1a\xf4\x02\n\x08Metadata\x12\x32\n\x07hashtag\x18\x01 \x01(\x0b\x32\x1c.celaut.Any.Metadata.HashTagH\x00\x88\x01\x01\x12%\n\x06\x66ormat\x18\x02 \x01(\x0b\x32\x10.celaut.FieldDefH\x01\x88\x01\x01\x1a\xf5\x01\n\x07HashTag\x12/\n\x04hash\x18\x01 \x03(\x0b\x32!.celaut.Any.Metadata.HashTag.Hash\x12\x0b\n\x03tag\x18\x02 \x03(\t\x12>\n\x0c\x61ttr_hashtag\x18\x03 \x03(\x0b\x32(.celaut.Any.Metadata.HashTag.AttrHashTag\x1a#\n\x04Hash\x12\x0c\n\x04type\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x1aG\n\x0b\x41ttrHashTag\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12+\n\x05value\x18\x02 \x03(\x0b\x32\x1c.celaut.Any.Metadata.HashTagB\n\n\x08_hashtagB\t\n\x07_formatB\x0b\n\t_metadata\"\xe2\x0f\n\x07Service\x12,\n\tcontainer\x18\x01 \x01(\x0b\x32\x19.celaut.Service.Container\x12 \n\x03\x61pi\x18\x02 \x01(\x0b\x32\x13.celaut.Service.Api\x12&\n\x06tensor\x18\x03 \x01(\x0b\x32\x16.celaut.Service.Tensor\x12&\n\x06ledger\x18\x04 \x01(\x0b\x32\x16.celaut.Service.Ledger\x1a\x81\x04\n\x03\x41pi\x12\x30\n\x0c\x61pp_protocol\x18\x01 \x01(\x0b\x32\x1a.celaut.Service.Api.AppDef\x12&\n\x04slot\x18\x02 \x03(\x0b\x32\x18.celaut.Service.Api.Slot\x12;\n\x0f\x63ontract_ledger\x18\x03 \x03(\x0b\x32\".celaut.Service.Api.ContractLedger\x1a\xe5\x01\n\x06\x41ppDef\x12\x36\n\x06method\x18\x01 \x03(\x0b\x32&.celaut.Service.Api.AppDef.MethodEntry\x1aN\n\tMethodDef\x12\x1f\n\x05input\x18\x01 \x01(\x0b\x32\x10.celaut.FieldDef\x12 \n\x06output\x18\x02 \x01(\x0b\x32\x10.celaut.FieldDef\x1aS\n\x0bMethodEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.celaut.Service.Api.AppDef.MethodDef:\x02\x38\x01\x1a\x30\n\x04Slot\x12\x0c\n\x04port\x18\x01 \x01(\x05\x12\x1a\n\x12transport_protocol\x18\x02 \x01(\x0c\x1aI\n\x0e\x43ontractLedger\x12\x10\n\x08\x63ontract\x18\x01 \x01(\x0c\x12\x15\n\rcontract_addr\x18\x02 \x01(\t\x12\x0e\n\x06ledger\x18\x03 \x01(\t\x1a\xb4\x06\n\tContainer\x12\x14\n\x0c\x61rchitecture\x18\x01 \x01(\x0c\x12\x12\n\nfilesystem\x18\x02 \x01(\x0c\x12P\n\x14\x65nviroment_variables\x18\x03 \x03(\x0b\x32\x32.celaut.Service.Container.EnviromentVariablesEntry\x12\x12\n\nentrypoint\x18\x04 \x03(\t\x12\x30\n\x06\x63onfig\x18\x05 \x01(\x0b\x32 .celaut.Service.Container.Config\x12\x43\n\x10\x65xpected_gateway\x18\x06 \x01(\x0b\x32).celaut.Service.Container.ExpectedGateway\x1a\xa6\x02\n\nFilesystem\x12?\n\x06\x62ranch\x18\x01 \x03(\x0b\x32/.celaut.Service.Container.Filesystem.ItemBranch\x1a\xd6\x01\n\nItemBranch\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x04\x66ile\x18\x02 \x01(\x0cH\x00\x12\x44\n\x04link\x18\x03 \x01(\x0b\x32\x34.celaut.Service.Container.Filesystem.ItemBranch.LinkH\x00\x12:\n\nfilesystem\x18\x04 \x01(\x0b\x32$.celaut.Service.Container.FilesystemH\x00\x1a \n\x04Link\x12\x0b\n\x03src\x18\x01 \x01(\t\x12\x0b\n\x03\x64st\x18\x02 \x01(\tB\x06\n\x04item\x1a\x38\n\x06\x43onfig\x12\x0c\n\x04path\x18\x01 \x03(\t\x12 \n\x06\x66ormat\x18\x02 \x01(\x0b\x32\x10.celaut.FieldDef\x1ao\n\x0f\x45xpectedGateway\x12\x38\n\x14gateway_app_protocol\x18\x01 \x01(\x0b\x32\x1a.celaut.Service.Api.AppDef\x12\"\n\x1agateway_transport_protocol\x18\x02 \x03(\x0c\x1aL\n\x18\x45nviromentVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.celaut.FieldDef:\x02\x38\x01\x1a\x88\x01\n\x06Tensor\x12\x30\n\x05index\x18\x01 \x03(\x0b\x32!.celaut.Service.Tensor.IndexEntry\x12\x0c\n\x04rank\x18\x02 \x01(\x05\x1a>\n\nIndexEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.celaut.FieldDef:\x02\x38\x01\x1a\xf0\x02\n\x06Ledger\x12:\n\rclass_diagram\x18\x01 \x01(\x0b\x32#.celaut.Service.Ledger.ClassDiagram\x12\x1f\n\x12\x63onsensus_protocol\x18\x02 \x01(\x0cH\x00\x88\x01\x01\x1a\xf1\x01\n\x0c\x43lassDiagram\x12?\n\x06\x63lases\x18\x01 \x03(\x0b\x32/.celaut.Service.Ledger.ClassDiagram.ClasesEntry\x1a@\n\x0bRelationDef\x12\x1f\n\x05\x66ield\x18\x01 \x01(\x0b\x32\x10.celaut.FieldDef\x12\x10\n\x08relation\x18\x02 \x01(\t\x1a^\n\x0b\x43lasesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12>\n\x05value\x18\x02 \x01(\x0b\x32/.celaut.Service.Ledger.ClassDiagram.RelationDef:\x02\x38\x01\x42\x15\n\x13_consensus_protocol\"\xc0\x01\n\x08Instance\x12 \n\x03\x61pi\x18\x01 \x01(\x0b\x32\x13.celaut.Service.Api\x12+\n\x08uri_slot\x18\x02 \x03(\x0b\x32\x19.celaut.Instance.Uri_Slot\x1a\x1f\n\x03Uri\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x1a\x44\n\x08Uri_Slot\x12\x15\n\rinternal_port\x18\x01 \x01(\x05\x12!\n\x03uri\x18\x02 \x03(\x0b\x32\x14.celaut.Instance.Uri\"\xac\x01\n\rConfiguration\x12L\n\x14\x65nviroment_variables\x18\x01 \x03(\x0b\x32..celaut.Configuration.EnviromentVariablesEntry\x12\x11\n\tspec_slot\x18\x02 \x03(\x05\x1a:\n\x18\x45nviromentVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\x91\x01\n\x11\x43onfigurationFile\x12!\n\x07gateway\x18\x01 \x01(\x0b\x32\x10.celaut.Instance\x12%\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x15.celaut.Configuration\x12\x32\n\x14initial_sysresources\x18\x03 \x01(\x0b\x32\x14.celaut.Sysresources\"\xd6\x01\n\x0cSysresources\x12\x19\n\x0c\x62lkio_weight\x18\x01 \x01(\x04H\x00\x88\x01\x01\x12\x17\n\ncpu_period\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12\x16\n\tcpu_quota\x18\x03 \x01(\x04H\x02\x88\x01\x01\x12\x16\n\tmem_limit\x18\x04 \x01(\x04H\x03\x88\x01\x01\x12\x17\n\ndisk_space\x18\x05 \x01(\x04H\x04\x88\x01\x01\x42\x0f\n\r_blkio_weightB\r\n\x0b_cpu_periodB\x0c\n\n_cpu_quotaB\x0c\n\n_mem_limitB\r\n\x0b_disk_spaceb\x06proto3')



_FIELDDEF = DESCRIPTOR.message_types_by_name['FieldDef']
_FIELDDEF_PRIMITIVEDEF = _FIELDDEF.nested_types_by_name['PrimitiveDef']
_FIELDDEF_ENUMDEF = _FIELDDEF.nested_types_by_name['EnumDef']
_FIELDDEF_ENUMDEF_VALUEENTRY = _FIELDDEF_ENUMDEF.nested_types_by_name['ValueEntry']
_FIELDDEF_MESSAGEDEF = _FIELDDEF.nested_types_by_name['MessageDef']
_FIELDDEF_MESSAGEDEF_PARAMDEF = _FIELDDEF_MESSAGEDEF.nested_types_by_name['ParamDef']
_FIELDDEF_MESSAGEDEF_ONEOFDEF = _FIELDDEF_MESSAGEDEF.nested_types_by_name['OneofDef']
_FIELDDEF_MESSAGEDEF_PARAMENTRY = _FIELDDEF_MESSAGEDEF.nested_types_by_name['ParamEntry']
_ANY = DESCRIPTOR.message_types_by_name['Any']
_ANY_METADATA = _ANY.nested_types_by_name['Metadata']
_ANY_METADATA_HASHTAG = _ANY_METADATA.nested_types_by_name['HashTag']
_ANY_METADATA_HASHTAG_HASH = _ANY_METADATA_HASHTAG.nested_types_by_name['Hash']
_ANY_METADATA_HASHTAG_ATTRHASHTAG = _ANY_METADATA_HASHTAG.nested_types_by_name['AttrHashTag']
_SERVICE = DESCRIPTOR.message_types_by_name['Service']
_SERVICE_API = _SERVICE.nested_types_by_name['Api']
_SERVICE_API_APPDEF = _SERVICE_API.nested_types_by_name['AppDef']
_SERVICE_API_APPDEF_METHODDEF = _SERVICE_API_APPDEF.nested_types_by_name['MethodDef']
_SERVICE_API_APPDEF_METHODENTRY = _SERVICE_API_APPDEF.nested_types_by_name['MethodEntry']
_SERVICE_API_SLOT = _SERVICE_API.nested_types_by_name['Slot']
_SERVICE_API_CONTRACTLEDGER = _SERVICE_API.nested_types_by_name['ContractLedger']
_SERVICE_CONTAINER = _SERVICE.nested_types_by_name['Container']
_SERVICE_CONTAINER_FILESYSTEM = _SERVICE_CONTAINER.nested_types_by_name['Filesystem']
_SERVICE_CONTAINER_FILESYSTEM_ITEMBRANCH = _SERVICE_CONTAINER_FILESYSTEM.nested_types_by_name['ItemBranch']
_SERVICE_CONTAINER_FILESYSTEM_ITEMBRANCH_LINK = _SERVICE_CONTAINER_FILESYSTEM_ITEMBRANCH.nested_types_by_name['Link']
_SERVICE_CONTAINER_CONFIG = _SERVICE_CONTAINER.nested_types_by_name['Config']
_SERVICE_CONTAINER_EXPECTEDGATEWAY = _SERVICE_CONTAINER.nested_types_by_name['ExpectedGateway']
_SERVICE_CONTAINER_ENVIROMENTVARIABLESENTRY = _SERVICE_CONTAINER.nested_types_by_name['EnviromentVariablesEntry']
_SERVICE_TENSOR = _SERVICE.nested_types_by_name['Tensor']
_SERVICE_TENSOR_INDEXENTRY = _SERVICE_TENSOR.nested_types_by_name['IndexEntry']
_SERVICE_LEDGER = _SERVICE.nested_types_by_name['Ledger']
_SERVICE_LEDGER_CLASSDIAGRAM = _SERVICE_LEDGER.nested_types_by_name['ClassDiagram']
_SERVICE_LEDGER_CLASSDIAGRAM_RELATIONDEF = _SERVICE_LEDGER_CLASSDIAGRAM.nested_types_by_name['RelationDef']
_SERVICE_LEDGER_CLASSDIAGRAM_CLASESENTRY = _SERVICE_LEDGER_CLASSDIAGRAM.nested_types_by_name['ClasesEntry']
_INSTANCE = DESCRIPTOR.message_types_by_name['Instance']
_INSTANCE_URI = _INSTANCE.nested_types_by_name['Uri']
_INSTANCE_URI_SLOT = _INSTANCE.nested_types_by_name['Uri_Slot']
_CONFIGURATION = DESCRIPTOR.message_types_by_name['Configuration']
_CONFIGURATION_ENVIROMENTVARIABLESENTRY = _CONFIGURATION.nested_types_by_name['EnviromentVariablesEntry']
_CONFIGURATIONFILE = DESCRIPTOR.message_types_by_name['ConfigurationFile']
_SYSRESOURCES = DESCRIPTOR.message_types_by_name['Sysresources']
FieldDef = _reflection.GeneratedProtocolMessageType('FieldDef', (_message.Message,), {

  'PrimitiveDef' : _reflection.GeneratedProtocolMessageType('PrimitiveDef', (_message.Message,), {
    'DESCRIPTOR' : _FIELDDEF_PRIMITIVEDEF,
    '__module__' : 'celaut_pb2'
    # @@protoc_insertion_point(class_scope:celaut.FieldDef.PrimitiveDef)
    })
  ,

  'EnumDef' : _reflection.GeneratedProtocolMessageType('EnumDef', (_message.Message,), {

    'ValueEntry' : _reflection.GeneratedProtocolMessageType('ValueEntry', (_message.Message,), {
      'DESCRIPTOR' : _FIELDDEF_ENUMDEF_VALUEENTRY,
      '__module__' : 'celaut_pb2'
      # @@protoc_insertion_point(class_scope:celaut.FieldDef.EnumDef.ValueEntry)
      })
    ,
    'DESCRIPTOR' : _FIELDDEF_ENUMDEF,
    '__module__' : 'celaut_pb2'
    # @@protoc_insertion_point(class_scope:celaut.FieldDef.EnumDef)
    })
  ,

  'MessageDef' : _reflection.GeneratedProtocolMessageType('MessageDef', (_message.Message,), {

    'ParamDef' : _reflection.GeneratedProtocolMessageType('ParamDef', (_message.Message,), {
      'DESCRIPTOR' : _FIELDDEF_MESSAGEDEF_PARAMDEF,
      '__module__' : 'celaut_pb2'
      # @@protoc_insertion_point(class_scope:celaut.FieldDef.MessageDef.ParamDef)
      })
    ,

    'OneofDef' : _reflection.GeneratedProtocolMessageType('OneofDef', (_message.Message,), {
      'DESCRIPTOR' : _FIELDDEF_MESSAGEDEF_ONEOFDEF,
      '__module__' : 'celaut_pb2'
      # @@protoc_insertion_point(class_scope:celaut.FieldDef.MessageDef.OneofDef)
      })
    ,

    'ParamEntry' : _reflection.GeneratedProtocolMessageType('ParamEntry', (_message.Message,), {
      'DESCRIPTOR' : _FIELDDEF_MESSAGEDEF_PARAMENTRY,
      '__module__' : 'celaut_pb2'
      # @@protoc_insertion_point(class_scope:celaut.FieldDef.MessageDef.ParamEntry)
      })
    ,
    'DESCRIPTOR' : _FIELDDEF_MESSAGEDEF,
    '__module__' : 'celaut_pb2'
    # @@protoc_insertion_point(class_scope:celaut.FieldDef.MessageDef)
    })
  ,
  'DESCRIPTOR' : _FIELDDEF,
  '__module__' : 'celaut_pb2'
  # @@protoc_insertion_point(class_scope:celaut.FieldDef)
  })
_sym_db.RegisterMessage(FieldDef)
_sym_db.RegisterMessage(FieldDef.PrimitiveDef)
_sym_db.RegisterMessage(FieldDef.EnumDef)
_sym_db.RegisterMessage(FieldDef.EnumDef.ValueEntry)
_sym_db.RegisterMessage(FieldDef.MessageDef)
_sym_db.RegisterMessage(FieldDef.MessageDef.ParamDef)
_sym_db.RegisterMessage(FieldDef.MessageDef.OneofDef)
_sym_db.RegisterMessage(FieldDef.MessageDef.ParamEntry)

Any = _reflection.GeneratedProtocolMessageType('Any', (_message.Message,), {

  'Metadata' : _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {

    'HashTag' : _reflection.GeneratedProtocolMessageType('HashTag', (_message.Message,), {

      'Hash' : _reflection.GeneratedProtocolMessageType('Hash', (_message.Message,), {
        'DESCRIPTOR' : _ANY_METADATA_HASHTAG_HASH,
        '__module__' : 'celaut_pb2'
        # @@protoc_insertion_point(class_scope:celaut.Any.Metadata.HashTag.Hash)
        })
      ,

      'AttrHashTag' : _reflection.GeneratedProtocolMessageType('AttrHashTag', (_message.Message,), {
        'DESCRIPTOR' : _ANY_METADATA_HASHTAG_ATTRHASHTAG,
        '__module__' : 'celaut_pb2'
        # @@protoc_insertion_point(class_scope:celaut.Any.Metadata.HashTag.AttrHashTag)
        })
      ,
      'DESCRIPTOR' : _ANY_METADATA_HASHTAG,
      '__module__' : 'celaut_pb2'
      # @@protoc_insertion_point(class_scope:celaut.Any.Metadata.HashTag)
      })
    ,
    'DESCRIPTOR' : _ANY_METADATA,
    '__module__' : 'celaut_pb2'
    # @@protoc_insertion_point(class_scope:celaut.Any.Metadata)
    })
  ,
  'DESCRIPTOR' : _ANY,
  '__module__' : 'celaut_pb2'
  # @@protoc_insertion_point(class_scope:celaut.Any)
  })
_sym_db.RegisterMessage(Any)
_sym_db.RegisterMessage(Any.Metadata)
_sym_db.RegisterMessage(Any.Metadata.HashTag)
_sym_db.RegisterMessage(Any.Metadata.HashTag.Hash)
_sym_db.RegisterMessage(Any.Metadata.HashTag.AttrHashTag)

Service = _reflection.GeneratedProtocolMessageType('Service', (_message.Message,), {

  'Api' : _reflection.GeneratedProtocolMessageType('Api', (_message.Message,), {

    'AppDef' : _reflection.GeneratedProtocolMessageType('AppDef', (_message.Message,), {

      'MethodDef' : _reflection.GeneratedProtocolMessageType('MethodDef', (_message.Message,), {
        'DESCRIPTOR' : _SERVICE_API_APPDEF_METHODDEF,
        '__module__' : 'celaut_pb2'
        # @@protoc_insertion_point(class_scope:celaut.Service.Api.AppDef.MethodDef)
        })
      ,

      'MethodEntry' : _reflection.GeneratedProtocolMessageType('MethodEntry', (_message.Message,), {
        'DESCRIPTOR' : _SERVICE_API_APPDEF_METHODENTRY,
        '__module__' : 'celaut_pb2'
        # @@protoc_insertion_point(class_scope:celaut.Service.Api.AppDef.MethodEntry)
        })
      ,
      'DESCRIPTOR' : _SERVICE_API_APPDEF,
      '__module__' : 'celaut_pb2'
      # @@protoc_insertion_point(class_scope:celaut.Service.Api.AppDef)
      })
    ,

    'Slot' : _reflection.GeneratedProtocolMessageType('Slot', (_message.Message,), {
      'DESCRIPTOR' : _SERVICE_API_SLOT,
      '__module__' : 'celaut_pb2'
      # @@protoc_insertion_point(class_scope:celaut.Service.Api.Slot)
      })
    ,

    'ContractLedger' : _reflection.GeneratedProtocolMessageType('ContractLedger', (_message.Message,), {
      'DESCRIPTOR' : _SERVICE_API_CONTRACTLEDGER,
      '__module__' : 'celaut_pb2'
      # @@protoc_insertion_point(class_scope:celaut.Service.Api.ContractLedger)
      })
    ,
    'DESCRIPTOR' : _SERVICE_API,
    '__module__' : 'celaut_pb2'
    # @@protoc_insertion_point(class_scope:celaut.Service.Api)
    })
  ,

  'Container' : _reflection.GeneratedProtocolMessageType('Container', (_message.Message,), {

    'Filesystem' : _reflection.GeneratedProtocolMessageType('Filesystem', (_message.Message,), {

      'ItemBranch' : _reflection.GeneratedProtocolMessageType('ItemBranch', (_message.Message,), {

        'Link' : _reflection.GeneratedProtocolMessageType('Link', (_message.Message,), {
          'DESCRIPTOR' : _SERVICE_CONTAINER_FILESYSTEM_ITEMBRANCH_LINK,
          '__module__' : 'celaut_pb2'
          # @@protoc_insertion_point(class_scope:celaut.Service.Container.Filesystem.ItemBranch.Link)
          })
        ,
        'DESCRIPTOR' : _SERVICE_CONTAINER_FILESYSTEM_ITEMBRANCH,
        '__module__' : 'celaut_pb2'
        # @@protoc_insertion_point(class_scope:celaut.Service.Container.Filesystem.ItemBranch)
        })
      ,
      'DESCRIPTOR' : _SERVICE_CONTAINER_FILESYSTEM,
      '__module__' : 'celaut_pb2'
      # @@protoc_insertion_point(class_scope:celaut.Service.Container.Filesystem)
      })
    ,

    'Config' : _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
      'DESCRIPTOR' : _SERVICE_CONTAINER_CONFIG,
      '__module__' : 'celaut_pb2'
      # @@protoc_insertion_point(class_scope:celaut.Service.Container.Config)
      })
    ,

    'ExpectedGateway' : _reflection.GeneratedProtocolMessageType('ExpectedGateway', (_message.Message,), {
      'DESCRIPTOR' : _SERVICE_CONTAINER_EXPECTEDGATEWAY,
      '__module__' : 'celaut_pb2'
      # @@protoc_insertion_point(class_scope:celaut.Service.Container.ExpectedGateway)
      })
    ,

    'EnviromentVariablesEntry' : _reflection.GeneratedProtocolMessageType('EnviromentVariablesEntry', (_message.Message,), {
      'DESCRIPTOR' : _SERVICE_CONTAINER_ENVIROMENTVARIABLESENTRY,
      '__module__' : 'celaut_pb2'
      # @@protoc_insertion_point(class_scope:celaut.Service.Container.EnviromentVariablesEntry)
      })
    ,
    'DESCRIPTOR' : _SERVICE_CONTAINER,
    '__module__' : 'celaut_pb2'
    # @@protoc_insertion_point(class_scope:celaut.Service.Container)
    })
  ,

  'Tensor' : _reflection.GeneratedProtocolMessageType('Tensor', (_message.Message,), {

    'IndexEntry' : _reflection.GeneratedProtocolMessageType('IndexEntry', (_message.Message,), {
      'DESCRIPTOR' : _SERVICE_TENSOR_INDEXENTRY,
      '__module__' : 'celaut_pb2'
      # @@protoc_insertion_point(class_scope:celaut.Service.Tensor.IndexEntry)
      })
    ,
    'DESCRIPTOR' : _SERVICE_TENSOR,
    '__module__' : 'celaut_pb2'
    # @@protoc_insertion_point(class_scope:celaut.Service.Tensor)
    })
  ,

  'Ledger' : _reflection.GeneratedProtocolMessageType('Ledger', (_message.Message,), {

    'ClassDiagram' : _reflection.GeneratedProtocolMessageType('ClassDiagram', (_message.Message,), {

      'RelationDef' : _reflection.GeneratedProtocolMessageType('RelationDef', (_message.Message,), {
        'DESCRIPTOR' : _SERVICE_LEDGER_CLASSDIAGRAM_RELATIONDEF,
        '__module__' : 'celaut_pb2'
        # @@protoc_insertion_point(class_scope:celaut.Service.Ledger.ClassDiagram.RelationDef)
        })
      ,

      'ClasesEntry' : _reflection.GeneratedProtocolMessageType('ClasesEntry', (_message.Message,), {
        'DESCRIPTOR' : _SERVICE_LEDGER_CLASSDIAGRAM_CLASESENTRY,
        '__module__' : 'celaut_pb2'
        # @@protoc_insertion_point(class_scope:celaut.Service.Ledger.ClassDiagram.ClasesEntry)
        })
      ,
      'DESCRIPTOR' : _SERVICE_LEDGER_CLASSDIAGRAM,
      '__module__' : 'celaut_pb2'
      # @@protoc_insertion_point(class_scope:celaut.Service.Ledger.ClassDiagram)
      })
    ,
    'DESCRIPTOR' : _SERVICE_LEDGER,
    '__module__' : 'celaut_pb2'
    # @@protoc_insertion_point(class_scope:celaut.Service.Ledger)
    })
  ,
  'DESCRIPTOR' : _SERVICE,
  '__module__' : 'celaut_pb2'
  # @@protoc_insertion_point(class_scope:celaut.Service)
  })
_sym_db.RegisterMessage(Service)
_sym_db.RegisterMessage(Service.Api)
_sym_db.RegisterMessage(Service.Api.AppDef)
_sym_db.RegisterMessage(Service.Api.AppDef.MethodDef)
_sym_db.RegisterMessage(Service.Api.AppDef.MethodEntry)
_sym_db.RegisterMessage(Service.Api.Slot)
_sym_db.RegisterMessage(Service.Api.ContractLedger)
_sym_db.RegisterMessage(Service.Container)
_sym_db.RegisterMessage(Service.Container.Filesystem)
_sym_db.RegisterMessage(Service.Container.Filesystem.ItemBranch)
_sym_db.RegisterMessage(Service.Container.Filesystem.ItemBranch.Link)
_sym_db.RegisterMessage(Service.Container.Config)
_sym_db.RegisterMessage(Service.Container.ExpectedGateway)
_sym_db.RegisterMessage(Service.Container.EnviromentVariablesEntry)
_sym_db.RegisterMessage(Service.Tensor)
_sym_db.RegisterMessage(Service.Tensor.IndexEntry)
_sym_db.RegisterMessage(Service.Ledger)
_sym_db.RegisterMessage(Service.Ledger.ClassDiagram)
_sym_db.RegisterMessage(Service.Ledger.ClassDiagram.RelationDef)
_sym_db.RegisterMessage(Service.Ledger.ClassDiagram.ClasesEntry)

Instance = _reflection.GeneratedProtocolMessageType('Instance', (_message.Message,), {

  'Uri' : _reflection.GeneratedProtocolMessageType('Uri', (_message.Message,), {
    'DESCRIPTOR' : _INSTANCE_URI,
    '__module__' : 'celaut_pb2'
    # @@protoc_insertion_point(class_scope:celaut.Instance.Uri)
    })
  ,

  'Uri_Slot' : _reflection.GeneratedProtocolMessageType('Uri_Slot', (_message.Message,), {
    'DESCRIPTOR' : _INSTANCE_URI_SLOT,
    '__module__' : 'celaut_pb2'
    # @@protoc_insertion_point(class_scope:celaut.Instance.Uri_Slot)
    })
  ,
  'DESCRIPTOR' : _INSTANCE,
  '__module__' : 'celaut_pb2'
  # @@protoc_insertion_point(class_scope:celaut.Instance)
  })
_sym_db.RegisterMessage(Instance)
_sym_db.RegisterMessage(Instance.Uri)
_sym_db.RegisterMessage(Instance.Uri_Slot)

Configuration = _reflection.GeneratedProtocolMessageType('Configuration', (_message.Message,), {

  'EnviromentVariablesEntry' : _reflection.GeneratedProtocolMessageType('EnviromentVariablesEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONFIGURATION_ENVIROMENTVARIABLESENTRY,
    '__module__' : 'celaut_pb2'
    # @@protoc_insertion_point(class_scope:celaut.Configuration.EnviromentVariablesEntry)
    })
  ,
  'DESCRIPTOR' : _CONFIGURATION,
  '__module__' : 'celaut_pb2'
  # @@protoc_insertion_point(class_scope:celaut.Configuration)
  })
_sym_db.RegisterMessage(Configuration)
_sym_db.RegisterMessage(Configuration.EnviromentVariablesEntry)

ConfigurationFile = _reflection.GeneratedProtocolMessageType('ConfigurationFile', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGURATIONFILE,
  '__module__' : 'celaut_pb2'
  # @@protoc_insertion_point(class_scope:celaut.ConfigurationFile)
  })
_sym_db.RegisterMessage(ConfigurationFile)

Sysresources = _reflection.GeneratedProtocolMessageType('Sysresources', (_message.Message,), {
  'DESCRIPTOR' : _SYSRESOURCES,
  '__module__' : 'celaut_pb2'
  # @@protoc_insertion_point(class_scope:celaut.Sysresources)
  })
_sym_db.RegisterMessage(Sysresources)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FIELDDEF_ENUMDEF_VALUEENTRY._options = None
  _FIELDDEF_ENUMDEF_VALUEENTRY._serialized_options = b'8\001'
  _FIELDDEF_MESSAGEDEF_PARAMENTRY._options = None
  _FIELDDEF_MESSAGEDEF_PARAMENTRY._serialized_options = b'8\001'
  _SERVICE_API_APPDEF_METHODENTRY._options = None
  _SERVICE_API_APPDEF_METHODENTRY._serialized_options = b'8\001'
  _SERVICE_CONTAINER_ENVIROMENTVARIABLESENTRY._options = None
  _SERVICE_CONTAINER_ENVIROMENTVARIABLESENTRY._serialized_options = b'8\001'
  _SERVICE_TENSOR_INDEXENTRY._options = None
  _SERVICE_TENSOR_INDEXENTRY._serialized_options = b'8\001'
  _SERVICE_LEDGER_CLASSDIAGRAM_CLASESENTRY._options = None
  _SERVICE_LEDGER_CLASSDIAGRAM_CLASESENTRY._serialized_options = b'8\001'
  _CONFIGURATION_ENVIROMENTVARIABLESENTRY._options = None
  _CONFIGURATION_ENVIROMENTVARIABLESENTRY._serialized_options = b'8\001'
  _FIELDDEF._serialized_start=25
  _FIELDDEF._serialized_end=638
  _FIELDDEF_PRIMITIVEDEF._serialized_start=179
  _FIELDDEF_PRIMITIVEDEF._serialized_end=223
  _FIELDDEF_ENUMDEF._serialized_start=225
  _FIELDDEF_ENUMDEF._serialized_end=332
  _FIELDDEF_ENUMDEF_VALUEENTRY._serialized_start=288
  _FIELDDEF_ENUMDEF_VALUEENTRY._serialized_end=332
  _FIELDDEF_MESSAGEDEF._serialized_start=335
  _FIELDDEF_MESSAGEDEF._serialized_end=629
  _FIELDDEF_MESSAGEDEF_PARAMDEF._serialized_start=457
  _FIELDDEF_MESSAGEDEF_PARAMDEF._serialized_end=518
  _FIELDDEF_MESSAGEDEF_ONEOFDEF._serialized_start=520
  _FIELDDEF_MESSAGEDEF_ONEOFDEF._serialized_end=545
  _FIELDDEF_MESSAGEDEF_PARAMENTRY._serialized_start=547
  _FIELDDEF_MESSAGEDEF_PARAMENTRY._serialized_end=629
  _ANY._serialized_start=641
  _ANY._serialized_end=1094
  _ANY_METADATA._serialized_start=709
  _ANY_METADATA._serialized_end=1081
  _ANY_METADATA_HASHTAG._serialized_start=813
  _ANY_METADATA_HASHTAG._serialized_end=1058
  _ANY_METADATA_HASHTAG_HASH._serialized_start=950
  _ANY_METADATA_HASHTAG_HASH._serialized_end=985
  _ANY_METADATA_HASHTAG_ATTRHASHTAG._serialized_start=987
  _ANY_METADATA_HASHTAG_ATTRHASHTAG._serialized_end=1058
  _SERVICE._serialized_start=1097
  _SERVICE._serialized_end=3115
  _SERVICE_API._serialized_start=1269
  _SERVICE_API._serialized_end=1782
  _SERVICE_API_APPDEF._serialized_start=1428
  _SERVICE_API_APPDEF._serialized_end=1657
  _SERVICE_API_APPDEF_METHODDEF._serialized_start=1494
  _SERVICE_API_APPDEF_METHODDEF._serialized_end=1572
  _SERVICE_API_APPDEF_METHODENTRY._serialized_start=1574
  _SERVICE_API_APPDEF_METHODENTRY._serialized_end=1657
  _SERVICE_API_SLOT._serialized_start=1659
  _SERVICE_API_SLOT._serialized_end=1707
  _SERVICE_API_CONTRACTLEDGER._serialized_start=1709
  _SERVICE_API_CONTRACTLEDGER._serialized_end=1782
  _SERVICE_CONTAINER._serialized_start=1785
  _SERVICE_CONTAINER._serialized_end=2605
  _SERVICE_CONTAINER_FILESYSTEM._serialized_start=2062
  _SERVICE_CONTAINER_FILESYSTEM._serialized_end=2356
  _SERVICE_CONTAINER_FILESYSTEM_ITEMBRANCH._serialized_start=2142
  _SERVICE_CONTAINER_FILESYSTEM_ITEMBRANCH._serialized_end=2356
  _SERVICE_CONTAINER_FILESYSTEM_ITEMBRANCH_LINK._serialized_start=2316
  _SERVICE_CONTAINER_FILESYSTEM_ITEMBRANCH_LINK._serialized_end=2348
  _SERVICE_CONTAINER_CONFIG._serialized_start=2358
  _SERVICE_CONTAINER_CONFIG._serialized_end=2414
  _SERVICE_CONTAINER_EXPECTEDGATEWAY._serialized_start=2416
  _SERVICE_CONTAINER_EXPECTEDGATEWAY._serialized_end=2527
  _SERVICE_CONTAINER_ENVIROMENTVARIABLESENTRY._serialized_start=2529
  _SERVICE_CONTAINER_ENVIROMENTVARIABLESENTRY._serialized_end=2605
  _SERVICE_TENSOR._serialized_start=2608
  _SERVICE_TENSOR._serialized_end=2744
  _SERVICE_TENSOR_INDEXENTRY._serialized_start=2682
  _SERVICE_TENSOR_INDEXENTRY._serialized_end=2744
  _SERVICE_LEDGER._serialized_start=2747
  _SERVICE_LEDGER._serialized_end=3115
  _SERVICE_LEDGER_CLASSDIAGRAM._serialized_start=2851
  _SERVICE_LEDGER_CLASSDIAGRAM._serialized_end=3092
  _SERVICE_LEDGER_CLASSDIAGRAM_RELATIONDEF._serialized_start=2932
  _SERVICE_LEDGER_CLASSDIAGRAM_RELATIONDEF._serialized_end=2996
  _SERVICE_LEDGER_CLASSDIAGRAM_CLASESENTRY._serialized_start=2998
  _SERVICE_LEDGER_CLASSDIAGRAM_CLASESENTRY._serialized_end=3092
  _INSTANCE._serialized_start=3118
  _INSTANCE._serialized_end=3310
  _INSTANCE_URI._serialized_start=3209
  _INSTANCE_URI._serialized_end=3240
  _INSTANCE_URI_SLOT._serialized_start=3242
  _INSTANCE_URI_SLOT._serialized_end=3310
  _CONFIGURATION._serialized_start=3313
  _CONFIGURATION._serialized_end=3485
  _CONFIGURATION_ENVIROMENTVARIABLESENTRY._serialized_start=3427
  _CONFIGURATION_ENVIROMENTVARIABLESENTRY._serialized_end=3485
  _CONFIGURATIONFILE._serialized_start=3488
  _CONFIGURATIONFILE._serialized_end=3633
  _SYSRESOURCES._serialized_start=3636
  _SYSRESOURCES._serialized_end=3850
# @@protoc_insertion_point(module_scope)
