# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: notification.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12notification.proto\"\xdb\x01\n\x13NotifyClientRequest\x12/\n\x0cupdated_item\x18\x01 \x01(\x0b\x32\x19.NotifyClientRequest.Item\x1a\x92\x01\n\x04Item\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05price\x18\x02 \x01(\x01\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x1a\n\x12quantity_remaining\x18\x06 \x01(\x05\x12\x0e\n\x06seller\x18\x07 \x01(\t\x12\x0e\n\x06rating\x18\x08 \x01(\x01\"&\n\x14NotifyClientResponse\x12\x0e\n\x06result\x18\x01 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'notification_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_NOTIFYCLIENTREQUEST']._serialized_start=23
  _globals['_NOTIFYCLIENTREQUEST']._serialized_end=242
  _globals['_NOTIFYCLIENTREQUEST_ITEM']._serialized_start=96
  _globals['_NOTIFYCLIENTREQUEST_ITEM']._serialized_end=242
  _globals['_NOTIFYCLIENTRESPONSE']._serialized_start=244
  _globals['_NOTIFYCLIENTRESPONSE']._serialized_end=282
# @@protoc_insertion_point(module_scope)
