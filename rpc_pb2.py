# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rpc.proto',
  package='rpc',
  syntax='proto3',
  serialized_pb=_b('\n\trpc.proto\x12\x03rpc\"B\n\nRPCRequest\x12\x12\n\nsession_id\x18\x01 \x01(\x0c\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\x12\x0f\n\x07version\x18\x03 \x01(\r\"\x8f\x01\n\x0bRPCResponse\x12\x12\n\nsession_id\x18\x01 \x01(\x0c\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\'\n\x06reason\x18\x03 \x01(\x0e\x32\x17.rpc.RPCResponse.Reason\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\x0c\"!\n\x06Reason\x12\x06\n\x02OK\x10\x00\x12\x0f\n\x0b\x42\x41\x44_REQUEST\x10\nB \n\x1eme.littlekey.duoyu.model.protob\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_RPCRESPONSE_REASON = _descriptor.EnumDescriptor(
  name='Reason',
  full_name='rpc.RPCResponse.Reason',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_REQUEST', index=1, number=10,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=197,
  serialized_end=230,
)
_sym_db.RegisterEnumDescriptor(_RPCRESPONSE_REASON)


_RPCREQUEST = _descriptor.Descriptor(
  name='RPCRequest',
  full_name='rpc.RPCRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='rpc.RPCRequest.session_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='rpc.RPCRequest.content', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='rpc.RPCRequest.version', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=84,
)


_RPCRESPONSE = _descriptor.Descriptor(
  name='RPCResponse',
  full_name='rpc.RPCResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='rpc.RPCResponse.session_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='success', full_name='rpc.RPCResponse.success', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='rpc.RPCResponse.reason', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='rpc.RPCResponse.content', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RPCRESPONSE_REASON,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=87,
  serialized_end=230,
)

_RPCRESPONSE.fields_by_name['reason'].enum_type = _RPCRESPONSE_REASON
_RPCRESPONSE_REASON.containing_type = _RPCRESPONSE
DESCRIPTOR.message_types_by_name['RPCRequest'] = _RPCREQUEST
DESCRIPTOR.message_types_by_name['RPCResponse'] = _RPCRESPONSE

RPCRequest = _reflection.GeneratedProtocolMessageType('RPCRequest', (_message.Message,), dict(
  DESCRIPTOR = _RPCREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:rpc.RPCRequest)
  ))
_sym_db.RegisterMessage(RPCRequest)

RPCResponse = _reflection.GeneratedProtocolMessageType('RPCResponse', (_message.Message,), dict(
  DESCRIPTOR = _RPCRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:rpc.RPCResponse)
  ))
_sym_db.RegisterMessage(RPCResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\036me.littlekey.duoyu.model.proto'))
# @@protoc_insertion_point(module_scope)
