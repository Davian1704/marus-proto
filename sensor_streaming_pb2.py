# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensor_streaming.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import geometry_pb2 as geometry__pb2
import sensor_pb2 as sensor__pb2
import marine_pb2 as marine__pb2
import geographic_pb2 as geographic__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sensor_streaming.proto',
  package='sensorstreaming',
  syntax='proto3',
  serialized_options=_b('\n io.grpc.examples.sensorstreamingB\017SensorStreamingP\001\242\002\003HLW'),
  serialized_pb=_b('\n\x16sensor_streaming.proto\x12\x0fsensorstreaming\x1a\x0egeometry.proto\x1a\x0csensor.proto\x1a\x0cmarine.proto\x1a\x10geographic.proto\"i\n\x16\x43\x61meraStreamingRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x11\n\ttimeStamp\x18\x02 \x01(\x01\x12\r\n\x05width\x18\x03 \x01(\r\x12\x0e\n\x06height\x18\x04 \x01(\r\x12\x0f\n\x07\x61\x64\x64ress\x18\x05 \x01(\t\"$\n\x11StreamingResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\xc8\x01\n\nPointField\x12\x0c\n\x04INT8\x18\x01 \x01(\r\x12\r\n\x05UINT8\x18\x02 \x01(\r\x12\r\n\x05INT16\x18\x03 \x01(\r\x12\x0e\n\x06UINT16\x18\x04 \x01(\r\x12\r\n\x05INT32\x18\x05 \x01(\r\x12\x0e\n\x06UINT32\x18\x06 \x01(\r\x12\x0f\n\x07\x46LOAT32\x18\x07 \x01(\r\x12\x0f\n\x07\x46LOAT64\x18\x08 \x01(\r\x12\x0c\n\x04name\x18\t \x01(\t\x12\x0e\n\x06offset\x18\n \x01(\r\x12\x10\n\x08\x64\x61tatype\x18\x0b \x01(\r\x12\r\n\x05\x63ount\x18\x0c \x01(\r\"\xd5\x01\n\x15LidarStreamingRequest\x12\x15\n\rtimeInSeconds\x18\x01 \x01(\x01\x12\x0e\n\x06height\x18\x02 \x01(\r\x12\r\n\x05width\x18\x03 \x01(\r\x12+\n\x06\x66ields\x18\x04 \x03(\x0b\x32\x1b.sensorstreaming.PointField\x12\x13\n\x0bisBigEndian\x18\x05 \x01(\x08\x12\x12\n\npoint_step\x18\x06 \x01(\r\x12\x10\n\x08row_step\x18\x07 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x08 \x01(\x0c\x12\x10\n\x08is_dense\x18\t \x01(\x08\"\xd3\x01\n\x15RadarStreamingRequest\x12\x16\n\x0erangeIncrement\x18\x01 \x01(\x02\x12\x12\n\nrangeStart\x18\x02 \x01(\x02\x12\x12\n\nnumSamples\x18\x03 \x01(\r\x12\x11\n\tnumSpokes\x18\x04 \x01(\r\x12\x14\n\x0cminIntensity\x18\x05 \x01(\r\x12\x14\n\x0cmaxIntensity\x18\x06 \x01(\r\x12\x15\n\rtimeInSeconds\x18\x07 \x03(\x01\x12\x0f\n\x07\x61zimuth\x18\x08 \x03(\x02\x12\x13\n\x0bradarSpokes\x18\t \x01(\x0c\"7\n\x15\x44\x65pthStreamingRequest\x12\r\n\x05\x64\x65pth\x18\x01 \x01(\x02\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\"A\n\x13\x44vlStreamingRequest\x12\x19\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x0b.marine.Dvl\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\"L\n\x14GnssStreamingRequest\x12#\n\x05point\x18\x01 \x01(\x0b\x32\x14.geographic.GeoPoint\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\"A\n\x13ImuStreamingRequest\x12\x19\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x0b.sensor.Imu\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\"E\n\x14PoseStreamingRequest\x12\x1c\n\x04pose\x18\x01 \x01(\x0b\x32\x0e.geometry.Pose\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\"H\n\x15SonarStreamingRequest\x12\r\n\x05range\x18\x01 \x01(\x02\x12\x0f\n\x07\x62\x65\x61ring\x18\x02 \x01(\x02\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\"\\\n\x13\x41ISStreamingRequest\x12\x34\n\x11\x61isPositionReport\x18\x01 \x01(\x0b\x32\x19.marine.AISPositionReport\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t2\xf5\x07\n\x0fSensorStreaming\x12\x65\n\x12StreamCameraSensor\x12\'.sensorstreaming.CameraStreamingRequest\x1a\".sensorstreaming.StreamingResponse\"\x00(\x01\x12\x63\n\x11StreamLidarSensor\x12&.sensorstreaming.LidarStreamingRequest\x1a\".sensorstreaming.StreamingResponse\"\x00(\x01\x12\x63\n\x11StreamRadarSensor\x12&.sensorstreaming.RadarStreamingRequest\x1a\".sensorstreaming.StreamingResponse\"\x00(\x01\x12\x63\n\x11StreamDepthSensor\x12&.sensorstreaming.DepthStreamingRequest\x1a\".sensorstreaming.StreamingResponse\"\x00(\x01\x12_\n\x0fStreamDvlSensor\x12$.sensorstreaming.DvlStreamingRequest\x1a\".sensorstreaming.StreamingResponse\"\x00(\x01\x12\x61\n\x10StreamGnssSensor\x12%.sensorstreaming.GnssStreamingRequest\x1a\".sensorstreaming.StreamingResponse\"\x00(\x01\x12_\n\x0fStreamImuSensor\x12$.sensorstreaming.ImuStreamingRequest\x1a\".sensorstreaming.StreamingResponse\"\x00(\x01\x12\x61\n\x10StreamPoseSensor\x12%.sensorstreaming.PoseStreamingRequest\x1a\".sensorstreaming.StreamingResponse\"\x00(\x01\x12\x63\n\x11StreamSonarSensor\x12&.sensorstreaming.SonarStreamingRequest\x1a\".sensorstreaming.StreamingResponse\"\x00(\x01\x12_\n\x0fStreamAisSensor\x12$.sensorstreaming.AISStreamingRequest\x1a\".sensorstreaming.StreamingResponse\"\x00(\x01\x42;\n io.grpc.examples.sensorstreamingB\x0fSensorStreamingP\x01\xa2\x02\x03HLWb\x06proto3')
  ,
  dependencies=[geometry__pb2.DESCRIPTOR,sensor__pb2.DESCRIPTOR,marine__pb2.DESCRIPTOR,geographic__pb2.DESCRIPTOR,])




_CAMERASTREAMINGREQUEST = _descriptor.Descriptor(
  name='CameraStreamingRequest',
  full_name='sensorstreaming.CameraStreamingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='sensorstreaming.CameraStreamingRequest.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='sensorstreaming.CameraStreamingRequest.timeStamp', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='sensorstreaming.CameraStreamingRequest.width', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='sensorstreaming.CameraStreamingRequest.height', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='sensorstreaming.CameraStreamingRequest.address', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=105,
  serialized_end=210,
)


_STREAMINGRESPONSE = _descriptor.Descriptor(
  name='StreamingResponse',
  full_name='sensorstreaming.StreamingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='sensorstreaming.StreamingResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=212,
  serialized_end=248,
)


_POINTFIELD = _descriptor.Descriptor(
  name='PointField',
  full_name='sensorstreaming.PointField',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='INT8', full_name='sensorstreaming.PointField.INT8', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='UINT8', full_name='sensorstreaming.PointField.UINT8', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='INT16', full_name='sensorstreaming.PointField.INT16', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='UINT16', full_name='sensorstreaming.PointField.UINT16', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='INT32', full_name='sensorstreaming.PointField.INT32', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='UINT32', full_name='sensorstreaming.PointField.UINT32', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FLOAT32', full_name='sensorstreaming.PointField.FLOAT32', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FLOAT64', full_name='sensorstreaming.PointField.FLOAT64', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='sensorstreaming.PointField.name', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='sensorstreaming.PointField.offset', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='datatype', full_name='sensorstreaming.PointField.datatype', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='sensorstreaming.PointField.count', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=251,
  serialized_end=451,
)


_LIDARSTREAMINGREQUEST = _descriptor.Descriptor(
  name='LidarStreamingRequest',
  full_name='sensorstreaming.LidarStreamingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeInSeconds', full_name='sensorstreaming.LidarStreamingRequest.timeInSeconds', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='sensorstreaming.LidarStreamingRequest.height', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='sensorstreaming.LidarStreamingRequest.width', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='sensorstreaming.LidarStreamingRequest.fields', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isBigEndian', full_name='sensorstreaming.LidarStreamingRequest.isBigEndian', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='point_step', full_name='sensorstreaming.LidarStreamingRequest.point_step', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='row_step', full_name='sensorstreaming.LidarStreamingRequest.row_step', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='sensorstreaming.LidarStreamingRequest.data', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_dense', full_name='sensorstreaming.LidarStreamingRequest.is_dense', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=454,
  serialized_end=667,
)


_RADARSTREAMINGREQUEST = _descriptor.Descriptor(
  name='RadarStreamingRequest',
  full_name='sensorstreaming.RadarStreamingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rangeIncrement', full_name='sensorstreaming.RadarStreamingRequest.rangeIncrement', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rangeStart', full_name='sensorstreaming.RadarStreamingRequest.rangeStart', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numSamples', full_name='sensorstreaming.RadarStreamingRequest.numSamples', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numSpokes', full_name='sensorstreaming.RadarStreamingRequest.numSpokes', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minIntensity', full_name='sensorstreaming.RadarStreamingRequest.minIntensity', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxIntensity', full_name='sensorstreaming.RadarStreamingRequest.maxIntensity', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeInSeconds', full_name='sensorstreaming.RadarStreamingRequest.timeInSeconds', index=6,
      number=7, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='azimuth', full_name='sensorstreaming.RadarStreamingRequest.azimuth', index=7,
      number=8, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radarSpokes', full_name='sensorstreaming.RadarStreamingRequest.radarSpokes', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=670,
  serialized_end=881,
)


_DEPTHSTREAMINGREQUEST = _descriptor.Descriptor(
  name='DepthStreamingRequest',
  full_name='sensorstreaming.DepthStreamingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='depth', full_name='sensorstreaming.DepthStreamingRequest.depth', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='sensorstreaming.DepthStreamingRequest.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=883,
  serialized_end=938,
)


_DVLSTREAMINGREQUEST = _descriptor.Descriptor(
  name='DvlStreamingRequest',
  full_name='sensorstreaming.DvlStreamingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='sensorstreaming.DvlStreamingRequest.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='sensorstreaming.DvlStreamingRequest.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=940,
  serialized_end=1005,
)


_GNSSSTREAMINGREQUEST = _descriptor.Descriptor(
  name='GnssStreamingRequest',
  full_name='sensorstreaming.GnssStreamingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='point', full_name='sensorstreaming.GnssStreamingRequest.point', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='sensorstreaming.GnssStreamingRequest.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1007,
  serialized_end=1083,
)


_IMUSTREAMINGREQUEST = _descriptor.Descriptor(
  name='ImuStreamingRequest',
  full_name='sensorstreaming.ImuStreamingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='sensorstreaming.ImuStreamingRequest.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='sensorstreaming.ImuStreamingRequest.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1085,
  serialized_end=1150,
)


_POSESTREAMINGREQUEST = _descriptor.Descriptor(
  name='PoseStreamingRequest',
  full_name='sensorstreaming.PoseStreamingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pose', full_name='sensorstreaming.PoseStreamingRequest.pose', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='sensorstreaming.PoseStreamingRequest.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1152,
  serialized_end=1221,
)


_SONARSTREAMINGREQUEST = _descriptor.Descriptor(
  name='SonarStreamingRequest',
  full_name='sensorstreaming.SonarStreamingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='range', full_name='sensorstreaming.SonarStreamingRequest.range', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bearing', full_name='sensorstreaming.SonarStreamingRequest.bearing', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='sensorstreaming.SonarStreamingRequest.address', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=1223,
  serialized_end=1295,
)


_AISSTREAMINGREQUEST = _descriptor.Descriptor(
  name='AISStreamingRequest',
  full_name='sensorstreaming.AISStreamingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='aisPositionReport', full_name='sensorstreaming.AISStreamingRequest.aisPositionReport', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='sensorstreaming.AISStreamingRequest.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1297,
  serialized_end=1389,
)

_LIDARSTREAMINGREQUEST.fields_by_name['fields'].message_type = _POINTFIELD
_DVLSTREAMINGREQUEST.fields_by_name['data'].message_type = marine__pb2._DVL
_GNSSSTREAMINGREQUEST.fields_by_name['point'].message_type = geographic__pb2._GEOPOINT
_IMUSTREAMINGREQUEST.fields_by_name['data'].message_type = sensor__pb2._IMU
_POSESTREAMINGREQUEST.fields_by_name['pose'].message_type = geometry__pb2._POSE
_AISSTREAMINGREQUEST.fields_by_name['aisPositionReport'].message_type = marine__pb2._AISPOSITIONREPORT
DESCRIPTOR.message_types_by_name['CameraStreamingRequest'] = _CAMERASTREAMINGREQUEST
DESCRIPTOR.message_types_by_name['StreamingResponse'] = _STREAMINGRESPONSE
DESCRIPTOR.message_types_by_name['PointField'] = _POINTFIELD
DESCRIPTOR.message_types_by_name['LidarStreamingRequest'] = _LIDARSTREAMINGREQUEST
DESCRIPTOR.message_types_by_name['RadarStreamingRequest'] = _RADARSTREAMINGREQUEST
DESCRIPTOR.message_types_by_name['DepthStreamingRequest'] = _DEPTHSTREAMINGREQUEST
DESCRIPTOR.message_types_by_name['DvlStreamingRequest'] = _DVLSTREAMINGREQUEST
DESCRIPTOR.message_types_by_name['GnssStreamingRequest'] = _GNSSSTREAMINGREQUEST
DESCRIPTOR.message_types_by_name['ImuStreamingRequest'] = _IMUSTREAMINGREQUEST
DESCRIPTOR.message_types_by_name['PoseStreamingRequest'] = _POSESTREAMINGREQUEST
DESCRIPTOR.message_types_by_name['SonarStreamingRequest'] = _SONARSTREAMINGREQUEST
DESCRIPTOR.message_types_by_name['AISStreamingRequest'] = _AISSTREAMINGREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CameraStreamingRequest = _reflection.GeneratedProtocolMessageType('CameraStreamingRequest', (_message.Message,), dict(
  DESCRIPTOR = _CAMERASTREAMINGREQUEST,
  __module__ = 'sensor_streaming_pb2'
  # @@protoc_insertion_point(class_scope:sensorstreaming.CameraStreamingRequest)
  ))
_sym_db.RegisterMessage(CameraStreamingRequest)

StreamingResponse = _reflection.GeneratedProtocolMessageType('StreamingResponse', (_message.Message,), dict(
  DESCRIPTOR = _STREAMINGRESPONSE,
  __module__ = 'sensor_streaming_pb2'
  # @@protoc_insertion_point(class_scope:sensorstreaming.StreamingResponse)
  ))
_sym_db.RegisterMessage(StreamingResponse)

PointField = _reflection.GeneratedProtocolMessageType('PointField', (_message.Message,), dict(
  DESCRIPTOR = _POINTFIELD,
  __module__ = 'sensor_streaming_pb2'
  # @@protoc_insertion_point(class_scope:sensorstreaming.PointField)
  ))
_sym_db.RegisterMessage(PointField)

LidarStreamingRequest = _reflection.GeneratedProtocolMessageType('LidarStreamingRequest', (_message.Message,), dict(
  DESCRIPTOR = _LIDARSTREAMINGREQUEST,
  __module__ = 'sensor_streaming_pb2'
  # @@protoc_insertion_point(class_scope:sensorstreaming.LidarStreamingRequest)
  ))
_sym_db.RegisterMessage(LidarStreamingRequest)

RadarStreamingRequest = _reflection.GeneratedProtocolMessageType('RadarStreamingRequest', (_message.Message,), dict(
  DESCRIPTOR = _RADARSTREAMINGREQUEST,
  __module__ = 'sensor_streaming_pb2'
  # @@protoc_insertion_point(class_scope:sensorstreaming.RadarStreamingRequest)
  ))
_sym_db.RegisterMessage(RadarStreamingRequest)

DepthStreamingRequest = _reflection.GeneratedProtocolMessageType('DepthStreamingRequest', (_message.Message,), dict(
  DESCRIPTOR = _DEPTHSTREAMINGREQUEST,
  __module__ = 'sensor_streaming_pb2'
  # @@protoc_insertion_point(class_scope:sensorstreaming.DepthStreamingRequest)
  ))
_sym_db.RegisterMessage(DepthStreamingRequest)

DvlStreamingRequest = _reflection.GeneratedProtocolMessageType('DvlStreamingRequest', (_message.Message,), dict(
  DESCRIPTOR = _DVLSTREAMINGREQUEST,
  __module__ = 'sensor_streaming_pb2'
  # @@protoc_insertion_point(class_scope:sensorstreaming.DvlStreamingRequest)
  ))
_sym_db.RegisterMessage(DvlStreamingRequest)

GnssStreamingRequest = _reflection.GeneratedProtocolMessageType('GnssStreamingRequest', (_message.Message,), dict(
  DESCRIPTOR = _GNSSSTREAMINGREQUEST,
  __module__ = 'sensor_streaming_pb2'
  # @@protoc_insertion_point(class_scope:sensorstreaming.GnssStreamingRequest)
  ))
_sym_db.RegisterMessage(GnssStreamingRequest)

ImuStreamingRequest = _reflection.GeneratedProtocolMessageType('ImuStreamingRequest', (_message.Message,), dict(
  DESCRIPTOR = _IMUSTREAMINGREQUEST,
  __module__ = 'sensor_streaming_pb2'
  # @@protoc_insertion_point(class_scope:sensorstreaming.ImuStreamingRequest)
  ))
_sym_db.RegisterMessage(ImuStreamingRequest)

PoseStreamingRequest = _reflection.GeneratedProtocolMessageType('PoseStreamingRequest', (_message.Message,), dict(
  DESCRIPTOR = _POSESTREAMINGREQUEST,
  __module__ = 'sensor_streaming_pb2'
  # @@protoc_insertion_point(class_scope:sensorstreaming.PoseStreamingRequest)
  ))
_sym_db.RegisterMessage(PoseStreamingRequest)

SonarStreamingRequest = _reflection.GeneratedProtocolMessageType('SonarStreamingRequest', (_message.Message,), dict(
  DESCRIPTOR = _SONARSTREAMINGREQUEST,
  __module__ = 'sensor_streaming_pb2'
  # @@protoc_insertion_point(class_scope:sensorstreaming.SonarStreamingRequest)
  ))
_sym_db.RegisterMessage(SonarStreamingRequest)

AISStreamingRequest = _reflection.GeneratedProtocolMessageType('AISStreamingRequest', (_message.Message,), dict(
  DESCRIPTOR = _AISSTREAMINGREQUEST,
  __module__ = 'sensor_streaming_pb2'
  # @@protoc_insertion_point(class_scope:sensorstreaming.AISStreamingRequest)
  ))
_sym_db.RegisterMessage(AISStreamingRequest)


DESCRIPTOR._options = None

_SENSORSTREAMING = _descriptor.ServiceDescriptor(
  name='SensorStreaming',
  full_name='sensorstreaming.SensorStreaming',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1392,
  serialized_end=2405,
  methods=[
  _descriptor.MethodDescriptor(
    name='StreamCameraSensor',
    full_name='sensorstreaming.SensorStreaming.StreamCameraSensor',
    index=0,
    containing_service=None,
    input_type=_CAMERASTREAMINGREQUEST,
    output_type=_STREAMINGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamLidarSensor',
    full_name='sensorstreaming.SensorStreaming.StreamLidarSensor',
    index=1,
    containing_service=None,
    input_type=_LIDARSTREAMINGREQUEST,
    output_type=_STREAMINGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamRadarSensor',
    full_name='sensorstreaming.SensorStreaming.StreamRadarSensor',
    index=2,
    containing_service=None,
    input_type=_RADARSTREAMINGREQUEST,
    output_type=_STREAMINGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamDepthSensor',
    full_name='sensorstreaming.SensorStreaming.StreamDepthSensor',
    index=3,
    containing_service=None,
    input_type=_DEPTHSTREAMINGREQUEST,
    output_type=_STREAMINGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamDvlSensor',
    full_name='sensorstreaming.SensorStreaming.StreamDvlSensor',
    index=4,
    containing_service=None,
    input_type=_DVLSTREAMINGREQUEST,
    output_type=_STREAMINGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamGnssSensor',
    full_name='sensorstreaming.SensorStreaming.StreamGnssSensor',
    index=5,
    containing_service=None,
    input_type=_GNSSSTREAMINGREQUEST,
    output_type=_STREAMINGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamImuSensor',
    full_name='sensorstreaming.SensorStreaming.StreamImuSensor',
    index=6,
    containing_service=None,
    input_type=_IMUSTREAMINGREQUEST,
    output_type=_STREAMINGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamPoseSensor',
    full_name='sensorstreaming.SensorStreaming.StreamPoseSensor',
    index=7,
    containing_service=None,
    input_type=_POSESTREAMINGREQUEST,
    output_type=_STREAMINGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamSonarSensor',
    full_name='sensorstreaming.SensorStreaming.StreamSonarSensor',
    index=8,
    containing_service=None,
    input_type=_SONARSTREAMINGREQUEST,
    output_type=_STREAMINGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamAisSensor',
    full_name='sensorstreaming.SensorStreaming.StreamAisSensor',
    index=9,
    containing_service=None,
    input_type=_AISSTREAMINGREQUEST,
    output_type=_STREAMINGRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SENSORSTREAMING)

DESCRIPTOR.services_by_name['SensorStreaming'] = _SENSORSTREAMING

# @@protoc_insertion_point(module_scope)
