steps = 0

def recurse(xyz):
	global steps
	if xyz == 1:
		print(steps)
	elif xyz % 2 == 0:
		xyz = xyz / 2
		steps += 1
		print(steps)
		recurse(xyz)
	else:
		xyz = (xyz * 3) + 1
		steps += 1
		print(steps)
		recurse(xyz)

def main():
	userInput = input("Recursively demonstrate Collatz Conjecture:" )
	recurse(int(userInput))

main()
