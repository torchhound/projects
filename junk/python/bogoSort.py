import random

def scramble(data):
	return random.sample(data, len(data))

def compare(data):
	ptr = 0 #something more elegant than a pointer?
	for x in len(data):
		if x <= data[ptr + 1]:
			continue
		else:
			return False
		ptr += 1

def main():
	test1 = []
	while True:
		compare(scramble(test1))

if __name__ == '__main__':
	main()