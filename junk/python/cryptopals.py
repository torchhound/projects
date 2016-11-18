import binascii

def hexToBase(hx):
	raw = binascii.unhexlify(hx)
	return binascii.b2a_base64(raw)

def main():
	print(hexToBase("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))

if __name__ == "__main__":
	main()
