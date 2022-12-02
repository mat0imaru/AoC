import numpy as np

class packet:
    def __init__(self, v, t, a) -> None:
        self.ver = v
        self.type = t
        self.values = a
    def getVersion(self):
        return self.ver
    def getType(self):
        return self.type
    def getValues(self):
        return self.values

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

def packet_parser(bin):
    ret = []
    pass

if __name__ == "__main__":
    hex = ''
    with open("Day16_input", 'r') as f:
        hex = f.readline()
    packets = []
    print(hex)
    print()
    print(hex2bin(hex))