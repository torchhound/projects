from base64 import encodestring

def hexToBase(hx):
	return encodestring(bytes(hx))

def main():
	print(hexToBase(0x49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d))

if __name__ == "__main__":
	main()
