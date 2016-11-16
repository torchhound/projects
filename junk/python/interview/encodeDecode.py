import struct

def encode(integer):
    '''Encodes an integer into a 4-character hexadecimal string'''
    raw = integer + 8192
    enH = struct.pack(">H", raw)
    final = enH.hex()
    return final

def decode(twoBytes):
    '''Decodes a two byte hexadecimal string into an integer between -8192 and 8191'''
    partial = int(twoBytes, 16)
    final = partial - 8192
    return final

def main():
    encoded  = [encode(6111), encode(340), encode(-2628), encode(-255), encode(7550)]
    dataFile = open("ConvertedData.txt", "w")
    for byte in encoded:
        print(byte)
        dataFile.write(str(byte) + "\n")    
    decoded = [decode("0A0A"), decode("0029"), decode("3F0F"), decode("4400"), decode("5E7F")]
    for hexa in decoded:
        print(hexa)
        dataFile.write(str(hexa) + "\n") 
    dataFile.close()

if __name__ == "__main__":
    main()

