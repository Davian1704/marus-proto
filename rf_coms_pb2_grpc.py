# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import rf_coms_pb2 as rf__coms__pb2
import std_pb2 as std__pb2


class RfTransmissionStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.StreamRangeingMsgs = channel.stream_unary(
        '/loracommunication.RfTransmission/StreamRangeingMsgs',
        request_serializer=rf__coms__pb2.RangeingMsg.SerializeToString,
        response_deserializer=std__pb2.Empty.FromString,
        )
    self.ReceiveLoraMessages = channel.unary_stream(
        '/loracommunication.RfTransmission/ReceiveLoraMessages',
        request_serializer=std__pb2.Empty.SerializeToString,
        response_deserializer=rf__coms__pb2.LoraMsg.FromString,
        )
    self.SendLoraMessage = channel.unary_unary(
        '/loracommunication.RfTransmission/SendLoraMessage',
        request_serializer=rf__coms__pb2.LoraMsg.SerializeToString,
        response_deserializer=std__pb2.Empty.FromString,
        )


class RfTransmissionServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def StreamRangeingMsgs(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReceiveLoraMessages(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendLoraMessage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RfTransmissionServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'StreamRangeingMsgs': grpc.stream_unary_rpc_method_handler(
          servicer.StreamRangeingMsgs,
          request_deserializer=rf__coms__pb2.RangeingMsg.FromString,
          response_serializer=std__pb2.Empty.SerializeToString,
      ),
      'ReceiveLoraMessages': grpc.unary_stream_rpc_method_handler(
          servicer.ReceiveLoraMessages,
          request_deserializer=std__pb2.Empty.FromString,
          response_serializer=rf__coms__pb2.LoraMsg.SerializeToString,
      ),
      'SendLoraMessage': grpc.unary_unary_rpc_method_handler(
          servicer.SendLoraMessage,
          request_deserializer=rf__coms__pb2.LoraMsg.FromString,
          response_serializer=std__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'loracommunication.RfTransmission', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
