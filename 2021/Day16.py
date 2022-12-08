import numpy as np

class literalPacket:
    def __init__(self, v, t, a):
        self.ver = v
        self.typeID = t
        self.values = a
        self.length = 3+3+len(self.values)*5
    def __str__(self) -> str:
        return f"version:{self.getVersion()},typeID:{self.getTypeID()},length:{self.getLength()},value:{self.getValues()}"
    def getVersion(self):
        return self.ver
    def getTypeID(self):
        return self.typeID
    def getValues(self):
        return self.values
    def getLength(self):
        return self.length

class operatorPacket:
    def __init__(self, v, t, i, l, s):
        self.ver = v
        self.typeID = t
        self.lengthTypeId = i
        self.length = l
        self.subPackets = s
    def __str__(self) -> str:
        return f"version:{self.getVersion()},typeID:{self.getTypeID()},lengthTypeID:{self.getLengthTypeID()},"
    def getVersion(self):
        return self.ver
    def getTypeID(self):
        return self.typeID
    def getLengthTypeID(self):
        return self.lengthTypeId
    def getLength(self):
        return self.length
    def getSubPackets(self):
        return self.subPackets
    
    
def hex2bin(hex):
    ret = ''
    hex2bin_map = {
        '0':'0000',
        '1':'0001',
        '2':'0010',
        '3':'0011',
        '4':'0100',
        '5':'0101',
        '6':'0110',
        '7':'0111',
        '8':'1000',
        '9':'1001',
        'A':'1010',
        'B':'1011',
        'C':'1100',
        'D':'1101',
        'E':'1110',
        'F':'1111',
    }
    for h in hex:
        ret += hex2bin_map[h]
    return ret

def parseLiteralPacket(bin, padding=False):
    i = 0
    version, bin = bin[:3], bin[3:]
    i += 3
    typeID, bin = bin[:3], bin[3:]
    i += 3
    if typeID == "100":
        print("literal value packet")
        values = []
        while True:
            prefix, value, bin = bin[:1], bin[1:5], bin[5:]
            i += 5
            values.append(value)
            if prefix == '0':
                if i%4 > 0:
                    if padding:
                        bin = bin[(4-i%4):]
                    i = 0
                break
        return literalPacket(version, typeID, values), bin
    else:
        return operatorPacket(version, typeID, '', '', []), bin

# def packet_parser(bin):
#     ret = []
#     while True:
#         packet, bin = parseLiteralPacket(bin)
#         if type(packet) == type(operatorPacket('','','','',[])):
#             print(bin)
#             lenTypeID, bin = bin[:1], bin[1:]
#             length = ''
#             if lenTypeID == '1':
#                 print("11-bit field")
#                 length, bin = bin[:11], bin[11:]
#                 intLength = 0
#             elif lenTypeID == '0':
#                 print("15-bit field")
#                 length, bin = bin[:15], bin[15:]
#             else:
#                 raise ValueError
#             intLength = 0
#             for i, bit in enumerate(length[::-1]):
#                 intLength += (2**i if bit == '1' else 0)
#             print(intLength)
#             packet.lengthTypeId = lenTypeID
#             packet.length = length
#             acc = 0
#             while acc < intLength:
#                 subPacket, bin = parseLiteralPacket(bin)
#                 packet.subPackets.append(subPacket)
#                 print(subPacket)
#                 acc += (subPacket.getLength() if packet.lengthTypeId == '0' else 1)
#                 # break
#             break
#     return ret

def packet_parser(bin):
    pass

if __name__ == "__main__":
    hex = ''
    bin = ''
    packets = []
    with open("Day16_input", 'r') as f:
        hex = f.readline()
    # bin = hex2bin(hex)
    bin = hex2bin("38006F45291200")
    print(bin)
    packets = packet_parser(bin)
