# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: business/diary.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model import model_pb2 as model_dot_model__pb2
import comment_pb2 as comment__pb2
from business import public_pb2 as business_dot_public__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='business/diary.proto',
  package='duoyu',
  syntax='proto3',
  serialized_pb=_b('\n\x14\x62usiness/diary.proto\x12\x05\x64uoyu\x1a\x11model/model.proto\x1a\rcomment.proto\x1a\x15\x62usiness/public.proto\"-\n\nHotRequest\x12\x1f\n\x06\x63ursor\x18\x01 \x01(\x0b\x32\x0f.comment.Cursor\"L\n\x0bHotResponse\x12\x1c\n\x06\x64iarys\x18\x01 \x03(\x0b\x32\x0c.model.Diary\x12\x1f\n\x06\x63ursor\x18\x02 \x01(\x0b\x32\x0f.comment.Cursor\"0\n\rRecentRequest\x12\x1f\n\x06\x63ursor\x18\x01 \x01(\x0b\x32\x0f.comment.Cursor\"O\n\x0eRecentResponse\x12\x1c\n\x06\x64iarys\x18\x01 \x03(\x0b\x32\x0c.model.Diary\x12\x1f\n\x06\x63ursor\x18\x02 \x01(\x0b\x32\x0f.comment.Cursor\"3\n\x10PublishedRequest\x12\x1f\n\x06\x63ursor\x18\x01 \x01(\x0b\x32\x0f.comment.Cursor\"O\n\x1bGetPublishedByUserIdRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x1f\n\x06\x63ursor\x18\x02 \x01(\x0b\x32\x0f.comment.Cursor\"R\n\x11PublishedResponse\x12\x1c\n\x06\x64iarys\x18\x01 \x03(\x0b\x32\x0c.model.Diary\x12\x1f\n\x06\x63ursor\x18\x02 \x01(\x0b\x32\x0f.comment.Cursor\".\n\x0fPutDiaryRequest\x12\x1b\n\x05\x64iary\x18\x01 \x01(\x0b\x32\x0c.model.Diary\"@\n\x10PutDiaryResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1b\n\x05\x64iary\x18\x02 \x01(\x0b\x32\x0c.model.Diary\"&\n\x12\x44\x65leteDiaryRequest\x12\x10\n\x08\x64iary_id\x18\x01 \x01(\t\"u\n\x13\x44\x65leteDiaryResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12/\n\x05\x65rrno\x18\x02 \x01(\x0e\x32 .duoyu.DeleteDiaryResponse.Errno\"\x1c\n\x05\x45rrno\x12\x13\n\x0fNOT_FOUND_DIARY\x10\x00\x32\x96\x04\n\x0c\x44iaryService\x12\x32\n\thotDiarys\x12\x11.duoyu.HotRequest\x1a\x12.duoyu.HotResponse\x12;\n\x0crecentDiarys\x12\x14.duoyu.RecentRequest\x1a\x15.duoyu.RecentResponse\x12\x44\n\x0fpublishedDiarys\x12\x17.duoyu.PublishedRequest\x1a\x18.duoyu.PublishedResponse\x12Z\n\x1agetPublishedDiarysByUserId\x12\".duoyu.GetPublishedByUserIdRequest\x1a\x18.duoyu.PublishedResponse\x12\x34\n\tlikeDiary\x12\x12.duoyu.LikeRequest\x1a\x13.duoyu.LikeResponse\x12:\n\x0bunlikeDiary\x12\x14.duoyu.UnlikeRequest\x1a\x15.duoyu.UnlikeResponse\x12;\n\x08putDiary\x12\x16.duoyu.PutDiaryRequest\x1a\x17.duoyu.PutDiaryResponse\x12\x44\n\x0b\x64\x65leteDiary\x12\x19.duoyu.DeleteDiaryRequest\x1a\x1a.duoyu.DeleteDiaryResponseB \n\x1eme.littlekey.duoyu.model.protob\x06proto3')
  ,
  dependencies=[model_dot_model__pb2.DESCRIPTOR,comment__pb2.DESCRIPTOR,business_dot_public__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_DELETEDIARYRESPONSE_ERRNO = _descriptor.EnumDescriptor(
  name='Errno',
  full_name='duoyu.DeleteDiaryResponse.Errno',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOT_FOUND_DIARY', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=805,
  serialized_end=833,
)
_sym_db.RegisterEnumDescriptor(_DELETEDIARYRESPONSE_ERRNO)


_HOTREQUEST = _descriptor.Descriptor(
  name='HotRequest',
  full_name='duoyu.HotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cursor', full_name='duoyu.HotRequest.cursor', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=88,
  serialized_end=133,
)


_HOTRESPONSE = _descriptor.Descriptor(
  name='HotResponse',
  full_name='duoyu.HotResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='diarys', full_name='duoyu.HotResponse.diarys', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cursor', full_name='duoyu.HotResponse.cursor', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=135,
  serialized_end=211,
)


_RECENTREQUEST = _descriptor.Descriptor(
  name='RecentRequest',
  full_name='duoyu.RecentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cursor', full_name='duoyu.RecentRequest.cursor', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=213,
  serialized_end=261,
)


_RECENTRESPONSE = _descriptor.Descriptor(
  name='RecentResponse',
  full_name='duoyu.RecentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='diarys', full_name='duoyu.RecentResponse.diarys', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cursor', full_name='duoyu.RecentResponse.cursor', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=263,
  serialized_end=342,
)


_PUBLISHEDREQUEST = _descriptor.Descriptor(
  name='PublishedRequest',
  full_name='duoyu.PublishedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cursor', full_name='duoyu.PublishedRequest.cursor', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=344,
  serialized_end=395,
)


_GETPUBLISHEDBYUSERIDREQUEST = _descriptor.Descriptor(
  name='GetPublishedByUserIdRequest',
  full_name='duoyu.GetPublishedByUserIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='duoyu.GetPublishedByUserIdRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cursor', full_name='duoyu.GetPublishedByUserIdRequest.cursor', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=397,
  serialized_end=476,
)


_PUBLISHEDRESPONSE = _descriptor.Descriptor(
  name='PublishedResponse',
  full_name='duoyu.PublishedResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='diarys', full_name='duoyu.PublishedResponse.diarys', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cursor', full_name='duoyu.PublishedResponse.cursor', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=478,
  serialized_end=560,
)


_PUTDIARYREQUEST = _descriptor.Descriptor(
  name='PutDiaryRequest',
  full_name='duoyu.PutDiaryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='diary', full_name='duoyu.PutDiaryRequest.diary', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=562,
  serialized_end=608,
)


_PUTDIARYRESPONSE = _descriptor.Descriptor(
  name='PutDiaryResponse',
  full_name='duoyu.PutDiaryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='duoyu.PutDiaryResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='diary', full_name='duoyu.PutDiaryResponse.diary', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=610,
  serialized_end=674,
)


_DELETEDIARYREQUEST = _descriptor.Descriptor(
  name='DeleteDiaryRequest',
  full_name='duoyu.DeleteDiaryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='diary_id', full_name='duoyu.DeleteDiaryRequest.diary_id', index=0,
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
  serialized_start=676,
  serialized_end=714,
)


_DELETEDIARYRESPONSE = _descriptor.Descriptor(
  name='DeleteDiaryResponse',
  full_name='duoyu.DeleteDiaryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='duoyu.DeleteDiaryResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errno', full_name='duoyu.DeleteDiaryResponse.errno', index=1,
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
    _DELETEDIARYRESPONSE_ERRNO,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=716,
  serialized_end=833,
)

_HOTREQUEST.fields_by_name['cursor'].message_type = comment__pb2._CURSOR
_HOTRESPONSE.fields_by_name['diarys'].message_type = model_dot_model__pb2._DIARY
_HOTRESPONSE.fields_by_name['cursor'].message_type = comment__pb2._CURSOR
_RECENTREQUEST.fields_by_name['cursor'].message_type = comment__pb2._CURSOR
_RECENTRESPONSE.fields_by_name['diarys'].message_type = model_dot_model__pb2._DIARY
_RECENTRESPONSE.fields_by_name['cursor'].message_type = comment__pb2._CURSOR
_PUBLISHEDREQUEST.fields_by_name['cursor'].message_type = comment__pb2._CURSOR
_GETPUBLISHEDBYUSERIDREQUEST.fields_by_name['cursor'].message_type = comment__pb2._CURSOR
_PUBLISHEDRESPONSE.fields_by_name['diarys'].message_type = model_dot_model__pb2._DIARY
_PUBLISHEDRESPONSE.fields_by_name['cursor'].message_type = comment__pb2._CURSOR
_PUTDIARYREQUEST.fields_by_name['diary'].message_type = model_dot_model__pb2._DIARY
_PUTDIARYRESPONSE.fields_by_name['diary'].message_type = model_dot_model__pb2._DIARY
_DELETEDIARYRESPONSE.fields_by_name['errno'].enum_type = _DELETEDIARYRESPONSE_ERRNO
_DELETEDIARYRESPONSE_ERRNO.containing_type = _DELETEDIARYRESPONSE
DESCRIPTOR.message_types_by_name['HotRequest'] = _HOTREQUEST
DESCRIPTOR.message_types_by_name['HotResponse'] = _HOTRESPONSE
DESCRIPTOR.message_types_by_name['RecentRequest'] = _RECENTREQUEST
DESCRIPTOR.message_types_by_name['RecentResponse'] = _RECENTRESPONSE
DESCRIPTOR.message_types_by_name['PublishedRequest'] = _PUBLISHEDREQUEST
DESCRIPTOR.message_types_by_name['GetPublishedByUserIdRequest'] = _GETPUBLISHEDBYUSERIDREQUEST
DESCRIPTOR.message_types_by_name['PublishedResponse'] = _PUBLISHEDRESPONSE
DESCRIPTOR.message_types_by_name['PutDiaryRequest'] = _PUTDIARYREQUEST
DESCRIPTOR.message_types_by_name['PutDiaryResponse'] = _PUTDIARYRESPONSE
DESCRIPTOR.message_types_by_name['DeleteDiaryRequest'] = _DELETEDIARYREQUEST
DESCRIPTOR.message_types_by_name['DeleteDiaryResponse'] = _DELETEDIARYRESPONSE

HotRequest = _reflection.GeneratedProtocolMessageType('HotRequest', (_message.Message,), dict(
  DESCRIPTOR = _HOTREQUEST,
  __module__ = 'business.diary_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.HotRequest)
  ))
_sym_db.RegisterMessage(HotRequest)

HotResponse = _reflection.GeneratedProtocolMessageType('HotResponse', (_message.Message,), dict(
  DESCRIPTOR = _HOTRESPONSE,
  __module__ = 'business.diary_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.HotResponse)
  ))
_sym_db.RegisterMessage(HotResponse)

RecentRequest = _reflection.GeneratedProtocolMessageType('RecentRequest', (_message.Message,), dict(
  DESCRIPTOR = _RECENTREQUEST,
  __module__ = 'business.diary_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.RecentRequest)
  ))
_sym_db.RegisterMessage(RecentRequest)

RecentResponse = _reflection.GeneratedProtocolMessageType('RecentResponse', (_message.Message,), dict(
  DESCRIPTOR = _RECENTRESPONSE,
  __module__ = 'business.diary_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.RecentResponse)
  ))
_sym_db.RegisterMessage(RecentResponse)

PublishedRequest = _reflection.GeneratedProtocolMessageType('PublishedRequest', (_message.Message,), dict(
  DESCRIPTOR = _PUBLISHEDREQUEST,
  __module__ = 'business.diary_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.PublishedRequest)
  ))
_sym_db.RegisterMessage(PublishedRequest)

GetPublishedByUserIdRequest = _reflection.GeneratedProtocolMessageType('GetPublishedByUserIdRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPUBLISHEDBYUSERIDREQUEST,
  __module__ = 'business.diary_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.GetPublishedByUserIdRequest)
  ))
_sym_db.RegisterMessage(GetPublishedByUserIdRequest)

PublishedResponse = _reflection.GeneratedProtocolMessageType('PublishedResponse', (_message.Message,), dict(
  DESCRIPTOR = _PUBLISHEDRESPONSE,
  __module__ = 'business.diary_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.PublishedResponse)
  ))
_sym_db.RegisterMessage(PublishedResponse)

PutDiaryRequest = _reflection.GeneratedProtocolMessageType('PutDiaryRequest', (_message.Message,), dict(
  DESCRIPTOR = _PUTDIARYREQUEST,
  __module__ = 'business.diary_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.PutDiaryRequest)
  ))
_sym_db.RegisterMessage(PutDiaryRequest)

PutDiaryResponse = _reflection.GeneratedProtocolMessageType('PutDiaryResponse', (_message.Message,), dict(
  DESCRIPTOR = _PUTDIARYRESPONSE,
  __module__ = 'business.diary_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.PutDiaryResponse)
  ))
_sym_db.RegisterMessage(PutDiaryResponse)

DeleteDiaryRequest = _reflection.GeneratedProtocolMessageType('DeleteDiaryRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEDIARYREQUEST,
  __module__ = 'business.diary_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.DeleteDiaryRequest)
  ))
_sym_db.RegisterMessage(DeleteDiaryRequest)

DeleteDiaryResponse = _reflection.GeneratedProtocolMessageType('DeleteDiaryResponse', (_message.Message,), dict(
  DESCRIPTOR = _DELETEDIARYRESPONSE,
  __module__ = 'business.diary_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.DeleteDiaryResponse)
  ))
_sym_db.RegisterMessage(DeleteDiaryResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\036me.littlekey.duoyu.model.proto'))
# @@protoc_insertion_point(module_scope)