import struct

def encode(integer):
    raw = integer + 8192
    enH = struct.pack(">H", raw)
    final = enH.hex()
    return final

def decode(twoBytes):
    if twoBytes not in range(0x7f):
        return False
    else:
        print(twoBytes)
        partial = bytes.fromhex(str(twoBytes))
        print(partial)
        return struct.unpack(">H", partial)

def main():
    encoded  = [encode(6111), encode(340), encode(-2628), encode(-255), encode(7550)]
    dataFile = open("ConvertedData.txt", "a")
    for byte in encoded:
        print(byte)
        dataFile.write(str(byte) + "\n")    
    decoded = [decode(0x0A0A), decode(0x0029), decode(0x3F0F), decode(0x4400), decode(0x5E7F)]
    for hexa in decoded:
        print(hexa)
        dataFile.write(str(hexa) + "\n") 

if __name__ == "__main__":
    main()

