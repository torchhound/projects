import binascii

def hexToBase(hx):
	raw = binascii.unhexlify(hx)
	return binascii.b2a_base64(raw)

def fixedXOR(b1, b2):
	r1 = binascii.unhexlify(b1)
	r2 = binascii.unhexlify(b2)
	final = bytearray(len(b1))
	for x in range(len(r1)):
		final[x] = r1[x] ^ r2[x]
	return binascii.hexlify(final)

def main():
	print(hexToBase("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))
	print(fixedXOR("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965"))

if __name__ == "__main__":
	main()
