# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mapReduce.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fmapReduce.proto\"L\n\x17InitializeMapperRequest\x12\x10\n\x08mapperId\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x03(\t\x12\x11\n\tcentroids\x18\x03 \x03(\t\"<\n\x18InitializeMapperResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"-\n\x18InitializeReducerRequest\x12\x11\n\treducerId\x18\x01 \x01(\x05\"=\n\x19InitializeReducerResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\">\n\x15\x46\x65tchPartitionRequest\x12\x10\n\x08mapperId\x18\x01 \x01(\x05\x12\x13\n\x0bpartitionId\x18\x02 \x01(\x05\"1\n\x16\x46\x65tchPartitionResponse\x12\x17\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\t.KeyValue\"&\n\x08KeyValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x19\n\x17\x43ompileCentroidsRequest\"O\n\x18\x43ompileCentroidsResponse\x12\x11\n\tcentroids\x18\x01 \x03(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x0f\n\x07message\x18\x03 \x01(\t\"\x1d\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\"#\n\tPointList\x12\x16\n\x06points\x18\x01 \x03(\x0b\x32\x06.Point\"=\n\nMapRequest\x12\x14\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x06.Point\x12\x19\n\tcentroids\x18\x02 \x03(\x0b\x32\x06.Point\"E\n\x0bMapResponse\x12\x14\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x06.Point\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x0f\n\x07message\x18\x03 \x01(\t2\xe3\x02\n\x10MapReduceService\x12I\n\x10InitializeMapper\x12\x18.InitializeMapperRequest\x1a\x19.InitializeMapperResponse\"\x00\x12\"\n\x03Map\x12\x0b.MapRequest\x1a\x0c.MapResponse\"\x00\x12L\n\x11InitializeReducer\x12\x19.InitializeReducerRequest\x1a\x1a.InitializeReducerResponse\"\x00\x12G\n\x12\x46\x65tchPartitionData\x12\x16.FetchPartitionRequest\x1a\x17.FetchPartitionResponse\"\x00\x12I\n\x10\x43ompileCentroids\x12\x18.CompileCentroidsRequest\x1a\x19.CompileCentroidsResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mapReduce_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_INITIALIZEMAPPERREQUEST']._serialized_start=19
  _globals['_INITIALIZEMAPPERREQUEST']._serialized_end=95
  _globals['_INITIALIZEMAPPERRESPONSE']._serialized_start=97
  _globals['_INITIALIZEMAPPERRESPONSE']._serialized_end=157
  _globals['_INITIALIZEREDUCERREQUEST']._serialized_start=159
  _globals['_INITIALIZEREDUCERREQUEST']._serialized_end=204
  _globals['_INITIALIZEREDUCERRESPONSE']._serialized_start=206
  _globals['_INITIALIZEREDUCERRESPONSE']._serialized_end=267
  _globals['_FETCHPARTITIONREQUEST']._serialized_start=269
  _globals['_FETCHPARTITIONREQUEST']._serialized_end=331
  _globals['_FETCHPARTITIONRESPONSE']._serialized_start=333
  _globals['_FETCHPARTITIONRESPONSE']._serialized_end=382
  _globals['_KEYVALUE']._serialized_start=384
  _globals['_KEYVALUE']._serialized_end=422
  _globals['_COMPILECENTROIDSREQUEST']._serialized_start=424
  _globals['_COMPILECENTROIDSREQUEST']._serialized_end=449
  _globals['_COMPILECENTROIDSRESPONSE']._serialized_start=451
  _globals['_COMPILECENTROIDSRESPONSE']._serialized_end=530
  _globals['_POINT']._serialized_start=532
  _globals['_POINT']._serialized_end=561
  _globals['_POINTLIST']._serialized_start=563
  _globals['_POINTLIST']._serialized_end=598
  _globals['_MAPREQUEST']._serialized_start=600
  _globals['_MAPREQUEST']._serialized_end=661
  _globals['_MAPRESPONSE']._serialized_start=663
  _globals['_MAPRESPONSE']._serialized_end=732
  _globals['_MAPREDUCESERVICE']._serialized_start=735
  _globals['_MAPREDUCESERVICE']._serialized_end=1090
# @@protoc_insertion_point(module_scope)
