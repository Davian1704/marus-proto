# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: labust.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import std_pb2 as std__pb2
import geographic_pb2 as geographic__pb2
import geometry_pb2 as geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='labust.proto',
  package='labust',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0clabust.proto\x12\x06labust\x1a\tstd.proto\x1a\x10geographic.proto\x1a\x0egeometry.proto\"\x8d\x02\n\nFSPathInfo\x12\x1b\n\x06header\x18\x01 \x01(\x0b\x32\x0b.std.Header\x12\x0e\n\x06\x64\x65ltaR\x18\x02 \x01(\x01\x12\t\n\x01k\x18\x03 \x01(\x01\x12\x0b\n\x03xiR\x18\x04 \x01(\x01\x12\x0c\n\x04\x64xiR\x18\x05 \x01(\x01\x12\n\n\x02pi\x18\x06 \x01(\x01\x12\x0f\n\x07piTilda\x18\x07 \x01(\x01\x12\x1e\n\x03\x64rP\x18\x08 \x01(\x0b\x32\x11.geometry.Vector3\x12#\n\x08position\x18\t \x01(\x0b\x32\x11.geometry.Vector3\x12&\n\x0borientation\x18\n \x01(\x0b\x32\x11.geometry.Vector3\x12\x11\n\tcurvature\x18\x0b \x01(\x01\x12\x0f\n\x07torsion\x18\x0c \x01(\x01\"\xfd\x01\n\x17PointerPrimitiveService\x12\x0e\n\x06radius\x18\x01 \x01(\x01\x12\x17\n\x0fvertical_offset\x18\x02 \x01(\x01\x12)\n\x0eguidanceTarget\x18\x03 \x01(\x0b\x32\x11.geometry.Vector3\x12\x16\n\x0eguidanceEnable\x18\x04 \x01(\x08\x12\x16\n\x0ewrappingEnable\x18\x05 \x01(\x08\x12\x13\n\x0b\x66ovGuidance\x18\x06 \x01(\x08\x12\x1d\n\x15streamlineOrientation\x18\x07 \x01(\x08\x12\x15\n\rguidanceTopic\x18\x08 \x01(\t\x12\x13\n\x0bradiusTopic\x18\t \x01(\tb\x06proto3')
  ,
  dependencies=[std__pb2.DESCRIPTOR,geographic__pb2.DESCRIPTOR,geometry__pb2.DESCRIPTOR,])




_FSPATHINFO = _descriptor.Descriptor(
  name='FSPathInfo',
  full_name='labust.FSPathInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='labust.FSPathInfo.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deltaR', full_name='labust.FSPathInfo.deltaR', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='k', full_name='labust.FSPathInfo.k', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xiR', full_name='labust.FSPathInfo.xiR', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dxiR', full_name='labust.FSPathInfo.dxiR', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pi', full_name='labust.FSPathInfo.pi', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='piTilda', full_name='labust.FSPathInfo.piTilda', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='drP', full_name='labust.FSPathInfo.drP', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='labust.FSPathInfo.position', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='labust.FSPathInfo.orientation', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='curvature', full_name='labust.FSPathInfo.curvature', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='torsion', full_name='labust.FSPathInfo.torsion', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=339,
)


_POINTERPRIMITIVESERVICE = _descriptor.Descriptor(
  name='PointerPrimitiveService',
  full_name='labust.PointerPrimitiveService',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='radius', full_name='labust.PointerPrimitiveService.radius', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vertical_offset', full_name='labust.PointerPrimitiveService.vertical_offset', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='guidanceTarget', full_name='labust.PointerPrimitiveService.guidanceTarget', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='guidanceEnable', full_name='labust.PointerPrimitiveService.guidanceEnable', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wrappingEnable', full_name='labust.PointerPrimitiveService.wrappingEnable', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fovGuidance', full_name='labust.PointerPrimitiveService.fovGuidance', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='streamlineOrientation', full_name='labust.PointerPrimitiveService.streamlineOrientation', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='guidanceTopic', full_name='labust.PointerPrimitiveService.guidanceTopic', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radiusTopic', full_name='labust.PointerPrimitiveService.radiusTopic', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=342,
  serialized_end=595,
)

_FSPATHINFO.fields_by_name['header'].message_type = std__pb2._HEADER
_FSPATHINFO.fields_by_name['drP'].message_type = geometry__pb2._VECTOR3
_FSPATHINFO.fields_by_name['position'].message_type = geometry__pb2._VECTOR3
_FSPATHINFO.fields_by_name['orientation'].message_type = geometry__pb2._VECTOR3
_POINTERPRIMITIVESERVICE.fields_by_name['guidanceTarget'].message_type = geometry__pb2._VECTOR3
DESCRIPTOR.message_types_by_name['FSPathInfo'] = _FSPATHINFO
DESCRIPTOR.message_types_by_name['PointerPrimitiveService'] = _POINTERPRIMITIVESERVICE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FSPathInfo = _reflection.GeneratedProtocolMessageType('FSPathInfo', (_message.Message,), dict(
  DESCRIPTOR = _FSPATHINFO,
  __module__ = 'labust_pb2'
  # @@protoc_insertion_point(class_scope:labust.FSPathInfo)
  ))
_sym_db.RegisterMessage(FSPathInfo)

PointerPrimitiveService = _reflection.GeneratedProtocolMessageType('PointerPrimitiveService', (_message.Message,), dict(
  DESCRIPTOR = _POINTERPRIMITIVESERVICE,
  __module__ = 'labust_pb2'
  # @@protoc_insertion_point(class_scope:labust.PointerPrimitiveService)
  ))
_sym_db.RegisterMessage(PointerPrimitiveService)


# @@protoc_insertion_point(module_scope)
