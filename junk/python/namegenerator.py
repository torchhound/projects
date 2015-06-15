import random
import string
def main():
	try:
		length = int(raw_input("Length of name: "))
	except ValueError:
		print "Could you at least give me an actual number?"
		return False
	s = ""
	for i in range(length):
		s += random.choice(string.ascii_lowercase)
	print s
main()