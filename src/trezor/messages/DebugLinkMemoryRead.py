# Automatically generated by pb2py
# fmt: off
import protobuf as p


class DebugLinkMemoryRead(p.MessageType):
    MESSAGE_WIRE_TYPE = 110
    FIELDS = {
        1: ('address', p.UVarintType, 0),
        2: ('length', p.UVarintType, 0),
    }

    def __init__(
        self,
        address: int = None,
        length: int = None,
    ) -> None:
        self.address = address
        self.length = length
