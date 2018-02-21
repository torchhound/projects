import random

noRe = []

def scramble(data):
        global noRe
	new = random.sample(data, len(data))
	noRe.append(new)
	for z in noRe:
		if new == z:
			scramble(data)
		else:
			continue
	return new

def compare(data):
	ptr = 0 #something more elegant than a pointer?
	for x in data:
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
