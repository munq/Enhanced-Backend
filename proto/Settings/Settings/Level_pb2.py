# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Settings/Level.proto

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
  name='Settings/Level.proto',
  package='POGOProtos.Settings',
  syntax='proto3',
  serialized_pb=_b('\n\x14Settings/Level.proto\x12\x13POGOProtos.Settings\"I\n\x05Level\x12\x1b\n\x13trainer_cp_modifier\x18\x02 \x01(\x01\x12#\n\x1btrainer_difficulty_modifier\x18\x03 \x01(\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LEVEL = _descriptor.Descriptor(
  name='Level',
  full_name='POGOProtos.Settings.Level',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trainer_cp_modifier', full_name='POGOProtos.Settings.Level.trainer_cp_modifier', index=0,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trainer_difficulty_modifier', full_name='POGOProtos.Settings.Level.trainer_difficulty_modifier', index=1,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=45,
  serialized_end=118,
)

DESCRIPTOR.message_types_by_name['Level'] = _LEVEL

Level = _reflection.GeneratedProtocolMessageType('Level', (_message.Message,), dict(
  DESCRIPTOR = _LEVEL,
  __module__ = 'Settings.Level_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.Level)
  ))
_sym_db.RegisterMessage(Level)


# @@protoc_insertion_point(module_scope)
