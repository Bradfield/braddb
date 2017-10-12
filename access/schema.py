"""
In defining a schema, the basics of what we need are a width (in bytes)
as well as serialization and deserialization functions.
"""

import struct


class FieldType(object):
    pass


class Int32(FieldType):
    """
    An unsigned 32 bit integer
    """
    width = 4

    def serialize(self, obj):
        return struct.pack('I', obj)

    def deserialize(self, data):
        return struct.unpack('I', data)[0]


class Float32(FieldType):
    """
    A 32 bit float
    """
    width = 4

    def serialize(self, obj):
        return struct.pack('f', obj)

    def deserialize(self, data):
        return struct.unpack('f', data)[0]


class Char(FieldType):
    """
    A null-terminated utf-8 character string with pre-determined storage length
    """
    def __init__(self, length):
        self.length = length

    def serialize(self, obj):
        enc = obj.encode('utf-8')
        if len(enc) >= self.length:
            raise Exception('Given char is too long')
        return enc + b'\0' * (self.length - len(enc))

    def deserialize(self, data):
        return data.rstrip(b'\0').decode('utf-8')

    @property
    def width(self):
        return self.length


class Schema(object):
    def __init__(self, fields):
        self.fields = fields
        self.width = sum(f.width for _, f in fields)

    def serialize(self, items):
        """
        Return a byte sequence representing the serialized form of each
        field in items.
        """
        bs = b''
        for item, field in zip(items, self.fields):
            bs += field[1].serialize(item)
        return bs

    def deserialize(self, data):
        """
        Return a tuple of deserialized fields
        """
        output = []
        i = 0
        for _, field in self.fields:
            output.append(field.deserialize(data[i:i+field.width]))
            i += field.width
        return tuple(output)
