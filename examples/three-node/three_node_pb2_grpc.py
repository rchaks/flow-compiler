# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import three_node_pb2 as three__node__pb2


class ThreeNodeExampleStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.tokenize = channel.unary_unary(
        '/ThreeNodeExample/tokenize',
        request_serializer=three__node__pb2.SystemRequest.SerializeToString,
        response_deserializer=three__node__pb2.SystemResponse.FromString,
        )
    self.split = channel.unary_unary(
        '/ThreeNodeExample/split',
        request_serializer=three__node__pb2.SplitRequest.SerializeToString,
        response_deserializer=three__node__pb2.SplitResponse.FromString,
        )
    self.label = channel.unary_unary(
        '/ThreeNodeExample/label',
        request_serializer=three__node__pb2.LabelRequest.SerializeToString,
        response_deserializer=three__node__pb2.LabelResponse.FromString,
        )
    self.strtoint = channel.unary_unary(
        '/ThreeNodeExample/strtoint',
        request_serializer=three__node__pb2.ToiRequest.SerializeToString,
        response_deserializer=three__node__pb2.ToiResponse.FromString,
        )


class ThreeNodeExampleServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def tokenize(self, request, context):
    """the orchestrator entry point 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def split(self, request, context):
    """the methods for the three worker nodes 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def label(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def strtoint(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ThreeNodeExampleServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'tokenize': grpc.unary_unary_rpc_method_handler(
          servicer.tokenize,
          request_deserializer=three__node__pb2.SystemRequest.FromString,
          response_serializer=three__node__pb2.SystemResponse.SerializeToString,
      ),
      'split': grpc.unary_unary_rpc_method_handler(
          servicer.split,
          request_deserializer=three__node__pb2.SplitRequest.FromString,
          response_serializer=three__node__pb2.SplitResponse.SerializeToString,
      ),
      'label': grpc.unary_unary_rpc_method_handler(
          servicer.label,
          request_deserializer=three__node__pb2.LabelRequest.FromString,
          response_serializer=three__node__pb2.LabelResponse.SerializeToString,
      ),
      'strtoint': grpc.unary_unary_rpc_method_handler(
          servicer.strtoint,
          request_deserializer=three__node__pb2.ToiRequest.FromString,
          response_serializer=three__node__pb2.ToiResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ThreeNodeExample', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
