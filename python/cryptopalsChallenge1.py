import binascii
from string import ascii_lowercase

def hexToBase(hx):
	raw = binascii.unhexlify(hx)
	return binascii.b2a_base64(raw)

def fixedXOR(b1, b2):
	r1 = binascii.unhexlify(b1)
	r2 = binascii.unhexlify(b2)
	final = bytearray(len(r1))
	for x in range(len(r1)):
		final[x] = r1[x] ^ r2[x]
	return binascii.hexlify(final)

def XORCipher(string):
	raw = binascii.unhexlify(string)
	final = {}
	count = 0
	for y in ascii_lowercase:
		dec = bytearray(len(raw))
		for x in range(len(raw)):
			dec[x] = raw[x] ^ bytes(y, "ascii")
		final[count] = dec
		count += 1
	return final

def main():
	print(hexToBase("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))
	print(fixedXOR("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965"))
	print(XORCipher("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"))

if __name__ == "__main__":
	main()
