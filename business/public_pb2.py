# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: business/public.proto

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
  name='business/public.proto',
  package='duoyu',
  syntax='proto3',
  serialized_pb=_b('\n\x15\x62usiness/public.proto\x12\x05\x64uoyu\"\x1f\n\x0bLikeRequest\x12\x10\n\x08identity\x18\x01 \x01(\t\"d\n\x0cLikeResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12(\n\x05\x65rrno\x18\x02 \x01(\x0e\x32\x19.duoyu.LikeResponse.Errno\"\x19\n\x05\x45rrno\x12\x10\n\x0c\x41LREADY_LIKE\x10\x00\"!\n\rUnlikeRequest\x12\x10\n\x08identity\x18\x01 \x01(\t\"d\n\x0eUnlikeResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12*\n\x05\x65rrno\x18\x02 \x01(\x0e\x32\x1b.duoyu.UnlikeResponse.Errno\"\x15\n\x05\x45rrno\x12\x0c\n\x08NOT_LIKE\x10\x00\x42 \n\x1eme.littlekey.duoyu.model.protob\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_LIKERESPONSE_ERRNO = _descriptor.EnumDescriptor(
  name='Errno',
  full_name='duoyu.LikeResponse.Errno',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ALREADY_LIKE', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=140,
  serialized_end=165,
)
_sym_db.RegisterEnumDescriptor(_LIKERESPONSE_ERRNO)

_UNLIKERESPONSE_ERRNO = _descriptor.EnumDescriptor(
  name='Errno',
  full_name='duoyu.UnlikeResponse.Errno',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOT_LIKE', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=281,
  serialized_end=302,
)
_sym_db.RegisterEnumDescriptor(_UNLIKERESPONSE_ERRNO)


_LIKEREQUEST = _descriptor.Descriptor(
  name='LikeRequest',
  full_name='duoyu.LikeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identity', full_name='duoyu.LikeRequest.identity', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=32,
  serialized_end=63,
)


_LIKERESPONSE = _descriptor.Descriptor(
  name='LikeResponse',
  full_name='duoyu.LikeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='duoyu.LikeResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errno', full_name='duoyu.LikeResponse.errno', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LIKERESPONSE_ERRNO,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=165,
)


_UNLIKEREQUEST = _descriptor.Descriptor(
  name='UnlikeRequest',
  full_name='duoyu.UnlikeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identity', full_name='duoyu.UnlikeRequest.identity', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=167,
  serialized_end=200,
)


_UNLIKERESPONSE = _descriptor.Descriptor(
  name='UnlikeResponse',
  full_name='duoyu.UnlikeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='duoyu.UnlikeResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errno', full_name='duoyu.UnlikeResponse.errno', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _UNLIKERESPONSE_ERRNO,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=202,
  serialized_end=302,
)

_LIKERESPONSE.fields_by_name['errno'].enum_type = _LIKERESPONSE_ERRNO
_LIKERESPONSE_ERRNO.containing_type = _LIKERESPONSE
_UNLIKERESPONSE.fields_by_name['errno'].enum_type = _UNLIKERESPONSE_ERRNO
_UNLIKERESPONSE_ERRNO.containing_type = _UNLIKERESPONSE
DESCRIPTOR.message_types_by_name['LikeRequest'] = _LIKEREQUEST
DESCRIPTOR.message_types_by_name['LikeResponse'] = _LIKERESPONSE
DESCRIPTOR.message_types_by_name['UnlikeRequest'] = _UNLIKEREQUEST
DESCRIPTOR.message_types_by_name['UnlikeResponse'] = _UNLIKERESPONSE

LikeRequest = _reflection.GeneratedProtocolMessageType('LikeRequest', (_message.Message,), dict(
  DESCRIPTOR = _LIKEREQUEST,
  __module__ = 'business.public_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.LikeRequest)
  ))
_sym_db.RegisterMessage(LikeRequest)

LikeResponse = _reflection.GeneratedProtocolMessageType('LikeResponse', (_message.Message,), dict(
  DESCRIPTOR = _LIKERESPONSE,
  __module__ = 'business.public_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.LikeResponse)
  ))
_sym_db.RegisterMessage(LikeResponse)

UnlikeRequest = _reflection.GeneratedProtocolMessageType('UnlikeRequest', (_message.Message,), dict(
  DESCRIPTOR = _UNLIKEREQUEST,
  __module__ = 'business.public_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.UnlikeRequest)
  ))
_sym_db.RegisterMessage(UnlikeRequest)

UnlikeResponse = _reflection.GeneratedProtocolMessageType('UnlikeResponse', (_message.Message,), dict(
  DESCRIPTOR = _UNLIKERESPONSE,
  __module__ = 'business.public_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.UnlikeResponse)
  ))
_sym_db.RegisterMessage(UnlikeResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\036me.littlekey.duoyu.model.proto'))
# @@protoc_insertion_point(module_scope)