#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class StepResult:
  """
  Attributes:
   - predicted_state
   - next_state
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'predicted_state', None, None, ), # 1
    (2, TType.I32, 'next_state', None, None, ), # 2
  )

  def __init__(self, predicted_state=None, next_state=None,):
    self.predicted_state = predicted_state
    self.next_state = next_state

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.predicted_state = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.next_state = iprot.readI32()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('StepResult')
    if self.predicted_state is not None:
      oprot.writeFieldBegin('predicted_state', TType.I32, 1)
      oprot.writeI32(self.predicted_state)
      oprot.writeFieldEnd()
    if self.next_state is not None:
      oprot.writeFieldBegin('next_state', TType.I32, 2)
      oprot.writeI32(self.next_state)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.predicted_state is None:
      raise TProtocol.TProtocolException(message='Required field predicted_state is unset!')
    if self.next_state is None:
      raise TProtocol.TProtocolException(message='Required field next_state is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.predicted_state)
    value = (value * 31) ^ hash(self.next_state)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
