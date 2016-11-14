# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: business/user.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='business/user.proto',
  package='duoyu',
  syntax='proto3',
  serialized_pb=_b('\n\x13\x62usiness/user.proto\x12\x05\x64uoyu\x1a\x11model/model.proto\x1a\rcomment.proto\"\x10\n\x0e\x43urrentRequest\"=\n\x0f\x43urrentResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x19\n\x04user\x18\x02 \x01(\x0b\x32\x0b.model.User\"%\n\x12GetUserByIdRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"\x8f\x01\n\x13GetUserByIdResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x19\n\x04user\x18\x02 \x01(\x0b\x32\x0b.model.User\x12/\n\x05\x65rrno\x18\x03 \x01(\x0e\x32 .duoyu.GetUserByIdResponse.Errno\"\x1b\n\x05\x45rrno\x12\x12\n\x0eUSER_NOT_FOUND\x10\x00\" \n\rFollowRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"\xb1\x01\n\x0e\x46ollowResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12.\n\x0crelationship\x18\x02 \x01(\x0e\x32\x18.model.User.Relationship\x12*\n\x05\x65rrno\x18\x03 \x01(\x0e\x32\x1b.duoyu.FollowResponse.Errno\"2\n\x05\x45rrno\x12\x12\n\x0eUSER_NOT_FOUND\x10\x00\x12\x15\n\x11\x41LREADY_FOLLOWING\x10\x01\"\"\n\x0fUnfollowRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"\xb1\x01\n\x10UnfollowResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12.\n\x0crelationship\x18\x02 \x01(\x0e\x32\x18.model.User.Relationship\x12,\n\x05\x65rrno\x18\x03 \x01(\x0e\x32\x1d.duoyu.UnfollowResponse.Errno\".\n\x05\x45rrno\x12\x12\n\x0eUSER_NOT_FOUND\x10\x00\x12\x11\n\rNOT_FOLLOWING\x10\x01\"C\n\x0f\x46ollowerRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x1f\n\x06\x63ursor\x18\x02 \x01(\x0b\x32\x0f.comment.Cursor\".\n\x10\x46ollowerResponse\x12\x1a\n\x05users\x18\x01 \x03(\x0b\x32\x0b.model.User\"D\n\x10\x46ollowingRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x1f\n\x06\x63ursor\x18\x02 \x01(\x0b\x32\x0f.comment.Cursor\"/\n\x11\x46ollowingResponse\x12\x1a\n\x05users\x18\x01 \x03(\x0b\x32\x0b.model.User\"u\n\x15\x43hangePasswordRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x1f\n\x17\x65mail_verification_code\x18\x02 \x01(\t\x12,\n\x08password\x18\x03 \x01(\x0b\x32\x1a.comment.PrehashedPassword\"\x8b\x01\n\x16\x43hangePasswordResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x32\n\x05\x65rrno\x18\x02 \x01(\x0e\x32#.duoyu.ChangePasswordResponse.Errno\",\n\x05\x45rrno\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x16\n\x12INVALID_EMAIL_CODE\x10\x01\"2\n\x0fTimelineRequest\x12\x1f\n\x06\x63ursor\x18\x01 \x01(\x0b\x32\x0f.comment.Cursor\"N\n\x1aGetTimelineByUserIdRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x1f\n\x06\x63ursor\x18\x02 \x01(\x0b\x32\x0f.comment.Cursor\"8\n\x10TimelineResponse\x12$\n\nhappenings\x18\x01 \x03(\x0b\x32\x10.model.Happening\"#\n\x12UploadImageRequest\x12\r\n\x05image\x18\x01 \x01(\x0c\"\xa8\x01\n\x13UploadImageResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x10\n\x08image_id\x18\x02 \x01(\t\x12/\n\x05\x65rrno\x18\x03 \x01(\x0e\x32 .duoyu.UploadImageResponse.Errno\"=\n\x05\x45rrno\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x13\n\x0fIMAGE_TOO_LARGE\x10\x01\x12\x12\n\x0eUPLOAD_FAILURE\x10\x02\x32\xbb\x05\n\x0bUserService\x12<\n\x0b\x63urrentUser\x12\x15.duoyu.CurrentRequest\x1a\x16.duoyu.CurrentResponse\x12\x44\n\x0bgetUserById\x12\x19.duoyu.GetUserByIdRequest\x1a\x1a.duoyu.GetUserByIdResponse\x12\x39\n\nfollowUser\x12\x14.duoyu.FollowRequest\x1a\x15.duoyu.FollowResponse\x12?\n\x0cunfollowUser\x12\x16.duoyu.UnfollowRequest\x1a\x17.duoyu.UnfollowResponse\x12?\n\x0c\x66ollowerList\x12\x16.duoyu.FollowerRequest\x1a\x17.duoyu.FollowerResponse\x12\x42\n\rfollowingList\x12\x17.duoyu.FollowingRequest\x1a\x18.duoyu.FollowingResponse\x12M\n\x0e\x63hangePassword\x12\x1c.duoyu.ChangePasswordRequest\x1a\x1d.duoyu.ChangePasswordResponse\x12?\n\x0cUserTimeline\x12\x16.duoyu.TimelineRequest\x1a\x17.duoyu.TimelineResponse\x12Q\n\x13GetTimelineByUserId\x12!.duoyu.GetTimelineByUserIdRequest\x1a\x17.duoyu.TimelineResponse\x12\x44\n\x0buploadImage\x12\x19.duoyu.UploadImageRequest\x1a\x1a.duoyu.UploadImageResponseB \n\x1eme.littlekey.duoyu.model.protob\x06proto3')
  ,
  dependencies=[model_dot_model__pb2.DESCRIPTOR,comment__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GETUSERBYIDRESPONSE_ERRNO = _descriptor.EnumDescriptor(
  name='Errno',
  full_name='duoyu.GetUserByIdResponse.Errno',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='USER_NOT_FOUND', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=301,
  serialized_end=328,
)
_sym_db.RegisterEnumDescriptor(_GETUSERBYIDRESPONSE_ERRNO)

_FOLLOWRESPONSE_ERRNO = _descriptor.EnumDescriptor(
  name='Errno',
  full_name='duoyu.FollowResponse.Errno',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='USER_NOT_FOUND', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALREADY_FOLLOWING', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=492,
  serialized_end=542,
)
_sym_db.RegisterEnumDescriptor(_FOLLOWRESPONSE_ERRNO)

_UNFOLLOWRESPONSE_ERRNO = _descriptor.EnumDescriptor(
  name='Errno',
  full_name='duoyu.UnfollowResponse.Errno',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='USER_NOT_FOUND', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_FOLLOWING', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=712,
  serialized_end=758,
)
_sym_db.RegisterEnumDescriptor(_UNFOLLOWRESPONSE_ERRNO)

_CHANGEPASSWORDRESPONSE_ERRNO = _descriptor.EnumDescriptor(
  name='Errno',
  full_name='duoyu.ChangePasswordResponse.Errno',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_EMAIL_CODE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1211,
  serialized_end=1255,
)
_sym_db.RegisterEnumDescriptor(_CHANGEPASSWORDRESPONSE_ERRNO)

_UPLOADIMAGERESPONSE_ERRNO = _descriptor.EnumDescriptor(
  name='Errno',
  full_name='duoyu.UploadImageResponse.Errno',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE_TOO_LARGE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPLOAD_FAILURE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1592,
  serialized_end=1653,
)
_sym_db.RegisterEnumDescriptor(_UPLOADIMAGERESPONSE_ERRNO)


_CURRENTREQUEST = _descriptor.Descriptor(
  name='CurrentRequest',
  full_name='duoyu.CurrentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=64,
  serialized_end=80,
)


_CURRENTRESPONSE = _descriptor.Descriptor(
  name='CurrentResponse',
  full_name='duoyu.CurrentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='duoyu.CurrentResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user', full_name='duoyu.CurrentResponse.user', index=1,
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
  serialized_start=82,
  serialized_end=143,
)


_GETUSERBYIDREQUEST = _descriptor.Descriptor(
  name='GetUserByIdRequest',
  full_name='duoyu.GetUserByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='duoyu.GetUserByIdRequest.user_id', index=0,
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
  serialized_start=145,
  serialized_end=182,
)


_GETUSERBYIDRESPONSE = _descriptor.Descriptor(
  name='GetUserByIdResponse',
  full_name='duoyu.GetUserByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='duoyu.GetUserByIdResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user', full_name='duoyu.GetUserByIdResponse.user', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errno', full_name='duoyu.GetUserByIdResponse.errno', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETUSERBYIDRESPONSE_ERRNO,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=185,
  serialized_end=328,
)


_FOLLOWREQUEST = _descriptor.Descriptor(
  name='FollowRequest',
  full_name='duoyu.FollowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='duoyu.FollowRequest.user_id', index=0,
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
  serialized_start=330,
  serialized_end=362,
)


_FOLLOWRESPONSE = _descriptor.Descriptor(
  name='FollowResponse',
  full_name='duoyu.FollowResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='duoyu.FollowResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relationship', full_name='duoyu.FollowResponse.relationship', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errno', full_name='duoyu.FollowResponse.errno', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FOLLOWRESPONSE_ERRNO,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=365,
  serialized_end=542,
)


_UNFOLLOWREQUEST = _descriptor.Descriptor(
  name='UnfollowRequest',
  full_name='duoyu.UnfollowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='duoyu.UnfollowRequest.user_id', index=0,
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
  serialized_start=544,
  serialized_end=578,
)


_UNFOLLOWRESPONSE = _descriptor.Descriptor(
  name='UnfollowResponse',
  full_name='duoyu.UnfollowResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='duoyu.UnfollowResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relationship', full_name='duoyu.UnfollowResponse.relationship', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errno', full_name='duoyu.UnfollowResponse.errno', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _UNFOLLOWRESPONSE_ERRNO,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=581,
  serialized_end=758,
)


_FOLLOWERREQUEST = _descriptor.Descriptor(
  name='FollowerRequest',
  full_name='duoyu.FollowerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='duoyu.FollowerRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cursor', full_name='duoyu.FollowerRequest.cursor', index=1,
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
  serialized_start=760,
  serialized_end=827,
)


_FOLLOWERRESPONSE = _descriptor.Descriptor(
  name='FollowerResponse',
  full_name='duoyu.FollowerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='users', full_name='duoyu.FollowerResponse.users', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=829,
  serialized_end=875,
)


_FOLLOWINGREQUEST = _descriptor.Descriptor(
  name='FollowingRequest',
  full_name='duoyu.FollowingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='duoyu.FollowingRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cursor', full_name='duoyu.FollowingRequest.cursor', index=1,
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
  serialized_start=877,
  serialized_end=945,
)


_FOLLOWINGRESPONSE = _descriptor.Descriptor(
  name='FollowingResponse',
  full_name='duoyu.FollowingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='users', full_name='duoyu.FollowingResponse.users', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=947,
  serialized_end=994,
)


_CHANGEPASSWORDREQUEST = _descriptor.Descriptor(
  name='ChangePasswordRequest',
  full_name='duoyu.ChangePasswordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='duoyu.ChangePasswordRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='email_verification_code', full_name='duoyu.ChangePasswordRequest.email_verification_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='duoyu.ChangePasswordRequest.password', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=996,
  serialized_end=1113,
)


_CHANGEPASSWORDRESPONSE = _descriptor.Descriptor(
  name='ChangePasswordResponse',
  full_name='duoyu.ChangePasswordResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='duoyu.ChangePasswordResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errno', full_name='duoyu.ChangePasswordResponse.errno', index=1,
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
    _CHANGEPASSWORDRESPONSE_ERRNO,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1116,
  serialized_end=1255,
)


_TIMELINEREQUEST = _descriptor.Descriptor(
  name='TimelineRequest',
  full_name='duoyu.TimelineRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cursor', full_name='duoyu.TimelineRequest.cursor', index=0,
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
  serialized_start=1257,
  serialized_end=1307,
)


_GETTIMELINEBYUSERIDREQUEST = _descriptor.Descriptor(
  name='GetTimelineByUserIdRequest',
  full_name='duoyu.GetTimelineByUserIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='duoyu.GetTimelineByUserIdRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cursor', full_name='duoyu.GetTimelineByUserIdRequest.cursor', index=1,
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
  serialized_start=1309,
  serialized_end=1387,
)


_TIMELINERESPONSE = _descriptor.Descriptor(
  name='TimelineResponse',
  full_name='duoyu.TimelineResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='happenings', full_name='duoyu.TimelineResponse.happenings', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1389,
  serialized_end=1445,
)


_UPLOADIMAGEREQUEST = _descriptor.Descriptor(
  name='UploadImageRequest',
  full_name='duoyu.UploadImageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='duoyu.UploadImageRequest.image', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=1447,
  serialized_end=1482,
)


_UPLOADIMAGERESPONSE = _descriptor.Descriptor(
  name='UploadImageResponse',
  full_name='duoyu.UploadImageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='duoyu.UploadImageResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_id', full_name='duoyu.UploadImageResponse.image_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errno', full_name='duoyu.UploadImageResponse.errno', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _UPLOADIMAGERESPONSE_ERRNO,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1485,
  serialized_end=1653,
)

_CURRENTRESPONSE.fields_by_name['user'].message_type = model_dot_model__pb2._USER
_GETUSERBYIDRESPONSE.fields_by_name['user'].message_type = model_dot_model__pb2._USER
_GETUSERBYIDRESPONSE.fields_by_name['errno'].enum_type = _GETUSERBYIDRESPONSE_ERRNO
_GETUSERBYIDRESPONSE_ERRNO.containing_type = _GETUSERBYIDRESPONSE
_FOLLOWRESPONSE.fields_by_name['relationship'].enum_type = model_dot_model__pb2._USER_RELATIONSHIP
_FOLLOWRESPONSE.fields_by_name['errno'].enum_type = _FOLLOWRESPONSE_ERRNO
_FOLLOWRESPONSE_ERRNO.containing_type = _FOLLOWRESPONSE
_UNFOLLOWRESPONSE.fields_by_name['relationship'].enum_type = model_dot_model__pb2._USER_RELATIONSHIP
_UNFOLLOWRESPONSE.fields_by_name['errno'].enum_type = _UNFOLLOWRESPONSE_ERRNO
_UNFOLLOWRESPONSE_ERRNO.containing_type = _UNFOLLOWRESPONSE
_FOLLOWERREQUEST.fields_by_name['cursor'].message_type = comment__pb2._CURSOR
_FOLLOWERRESPONSE.fields_by_name['users'].message_type = model_dot_model__pb2._USER
_FOLLOWINGREQUEST.fields_by_name['cursor'].message_type = comment__pb2._CURSOR
_FOLLOWINGRESPONSE.fields_by_name['users'].message_type = model_dot_model__pb2._USER
_CHANGEPASSWORDREQUEST.fields_by_name['password'].message_type = comment__pb2._PREHASHEDPASSWORD
_CHANGEPASSWORDRESPONSE.fields_by_name['errno'].enum_type = _CHANGEPASSWORDRESPONSE_ERRNO
_CHANGEPASSWORDRESPONSE_ERRNO.containing_type = _CHANGEPASSWORDRESPONSE
_TIMELINEREQUEST.fields_by_name['cursor'].message_type = comment__pb2._CURSOR
_GETTIMELINEBYUSERIDREQUEST.fields_by_name['cursor'].message_type = comment__pb2._CURSOR
_TIMELINERESPONSE.fields_by_name['happenings'].message_type = model_dot_model__pb2._HAPPENING
_UPLOADIMAGERESPONSE.fields_by_name['errno'].enum_type = _UPLOADIMAGERESPONSE_ERRNO
_UPLOADIMAGERESPONSE_ERRNO.containing_type = _UPLOADIMAGERESPONSE
DESCRIPTOR.message_types_by_name['CurrentRequest'] = _CURRENTREQUEST
DESCRIPTOR.message_types_by_name['CurrentResponse'] = _CURRENTRESPONSE
DESCRIPTOR.message_types_by_name['GetUserByIdRequest'] = _GETUSERBYIDREQUEST
DESCRIPTOR.message_types_by_name['GetUserByIdResponse'] = _GETUSERBYIDRESPONSE
DESCRIPTOR.message_types_by_name['FollowRequest'] = _FOLLOWREQUEST
DESCRIPTOR.message_types_by_name['FollowResponse'] = _FOLLOWRESPONSE
DESCRIPTOR.message_types_by_name['UnfollowRequest'] = _UNFOLLOWREQUEST
DESCRIPTOR.message_types_by_name['UnfollowResponse'] = _UNFOLLOWRESPONSE
DESCRIPTOR.message_types_by_name['FollowerRequest'] = _FOLLOWERREQUEST
DESCRIPTOR.message_types_by_name['FollowerResponse'] = _FOLLOWERRESPONSE
DESCRIPTOR.message_types_by_name['FollowingRequest'] = _FOLLOWINGREQUEST
DESCRIPTOR.message_types_by_name['FollowingResponse'] = _FOLLOWINGRESPONSE
DESCRIPTOR.message_types_by_name['ChangePasswordRequest'] = _CHANGEPASSWORDREQUEST
DESCRIPTOR.message_types_by_name['ChangePasswordResponse'] = _CHANGEPASSWORDRESPONSE
DESCRIPTOR.message_types_by_name['TimelineRequest'] = _TIMELINEREQUEST
DESCRIPTOR.message_types_by_name['GetTimelineByUserIdRequest'] = _GETTIMELINEBYUSERIDREQUEST
DESCRIPTOR.message_types_by_name['TimelineResponse'] = _TIMELINERESPONSE
DESCRIPTOR.message_types_by_name['UploadImageRequest'] = _UPLOADIMAGEREQUEST
DESCRIPTOR.message_types_by_name['UploadImageResponse'] = _UPLOADIMAGERESPONSE

CurrentRequest = _reflection.GeneratedProtocolMessageType('CurrentRequest', (_message.Message,), dict(
  DESCRIPTOR = _CURRENTREQUEST,
  __module__ = 'business.user_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.CurrentRequest)
  ))
_sym_db.RegisterMessage(CurrentRequest)

CurrentResponse = _reflection.GeneratedProtocolMessageType('CurrentResponse', (_message.Message,), dict(
  DESCRIPTOR = _CURRENTRESPONSE,
  __module__ = 'business.user_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.CurrentResponse)
  ))
_sym_db.RegisterMessage(CurrentResponse)

GetUserByIdRequest = _reflection.GeneratedProtocolMessageType('GetUserByIdRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETUSERBYIDREQUEST,
  __module__ = 'business.user_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.GetUserByIdRequest)
  ))
_sym_db.RegisterMessage(GetUserByIdRequest)

GetUserByIdResponse = _reflection.GeneratedProtocolMessageType('GetUserByIdResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETUSERBYIDRESPONSE,
  __module__ = 'business.user_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.GetUserByIdResponse)
  ))
_sym_db.RegisterMessage(GetUserByIdResponse)

FollowRequest = _reflection.GeneratedProtocolMessageType('FollowRequest', (_message.Message,), dict(
  DESCRIPTOR = _FOLLOWREQUEST,
  __module__ = 'business.user_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.FollowRequest)
  ))
_sym_db.RegisterMessage(FollowRequest)

FollowResponse = _reflection.GeneratedProtocolMessageType('FollowResponse', (_message.Message,), dict(
  DESCRIPTOR = _FOLLOWRESPONSE,
  __module__ = 'business.user_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.FollowResponse)
  ))
_sym_db.RegisterMessage(FollowResponse)

UnfollowRequest = _reflection.GeneratedProtocolMessageType('UnfollowRequest', (_message.Message,), dict(
  DESCRIPTOR = _UNFOLLOWREQUEST,
  __module__ = 'business.user_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.UnfollowRequest)
  ))
_sym_db.RegisterMessage(UnfollowRequest)

UnfollowResponse = _reflection.GeneratedProtocolMessageType('UnfollowResponse', (_message.Message,), dict(
  DESCRIPTOR = _UNFOLLOWRESPONSE,
  __module__ = 'business.user_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.UnfollowResponse)
  ))
_sym_db.RegisterMessage(UnfollowResponse)

FollowerRequest = _reflection.GeneratedProtocolMessageType('FollowerRequest', (_message.Message,), dict(
  DESCRIPTOR = _FOLLOWERREQUEST,
  __module__ = 'business.user_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.FollowerRequest)
  ))
_sym_db.RegisterMessage(FollowerRequest)

FollowerResponse = _reflection.GeneratedProtocolMessageType('FollowerResponse', (_message.Message,), dict(
  DESCRIPTOR = _FOLLOWERRESPONSE,
  __module__ = 'business.user_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.FollowerResponse)
  ))
_sym_db.RegisterMessage(FollowerResponse)

FollowingRequest = _reflection.GeneratedProtocolMessageType('FollowingRequest', (_message.Message,), dict(
  DESCRIPTOR = _FOLLOWINGREQUEST,
  __module__ = 'business.user_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.FollowingRequest)
  ))
_sym_db.RegisterMessage(FollowingRequest)

FollowingResponse = _reflection.GeneratedProtocolMessageType('FollowingResponse', (_message.Message,), dict(
  DESCRIPTOR = _FOLLOWINGRESPONSE,
  __module__ = 'business.user_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.FollowingResponse)
  ))
_sym_db.RegisterMessage(FollowingResponse)

ChangePasswordRequest = _reflection.GeneratedProtocolMessageType('ChangePasswordRequest', (_message.Message,), dict(
  DESCRIPTOR = _CHANGEPASSWORDREQUEST,
  __module__ = 'business.user_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.ChangePasswordRequest)
  ))
_sym_db.RegisterMessage(ChangePasswordRequest)

ChangePasswordResponse = _reflection.GeneratedProtocolMessageType('ChangePasswordResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHANGEPASSWORDRESPONSE,
  __module__ = 'business.user_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.ChangePasswordResponse)
  ))
_sym_db.RegisterMessage(ChangePasswordResponse)

TimelineRequest = _reflection.GeneratedProtocolMessageType('TimelineRequest', (_message.Message,), dict(
  DESCRIPTOR = _TIMELINEREQUEST,
  __module__ = 'business.user_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.TimelineRequest)
  ))
_sym_db.RegisterMessage(TimelineRequest)

GetTimelineByUserIdRequest = _reflection.GeneratedProtocolMessageType('GetTimelineByUserIdRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETTIMELINEBYUSERIDREQUEST,
  __module__ = 'business.user_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.GetTimelineByUserIdRequest)
  ))
_sym_db.RegisterMessage(GetTimelineByUserIdRequest)

TimelineResponse = _reflection.GeneratedProtocolMessageType('TimelineResponse', (_message.Message,), dict(
  DESCRIPTOR = _TIMELINERESPONSE,
  __module__ = 'business.user_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.TimelineResponse)
  ))
_sym_db.RegisterMessage(TimelineResponse)

UploadImageRequest = _reflection.GeneratedProtocolMessageType('UploadImageRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPLOADIMAGEREQUEST,
  __module__ = 'business.user_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.UploadImageRequest)
  ))
_sym_db.RegisterMessage(UploadImageRequest)

UploadImageResponse = _reflection.GeneratedProtocolMessageType('UploadImageResponse', (_message.Message,), dict(
  DESCRIPTOR = _UPLOADIMAGERESPONSE,
  __module__ = 'business.user_pb2'
  # @@protoc_insertion_point(class_scope:duoyu.UploadImageResponse)
  ))
_sym_db.RegisterMessage(UploadImageResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\036me.littlekey.duoyu.model.proto'))
# @@protoc_insertion_point(module_scope)