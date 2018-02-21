def conjecture(y):
	steps = 0
	number = int(y)
	while number > 1:
		steps += 1
		if number % 2 == 0:
			number = number / 2
		else:
			number = (number * 3) + 1
		print(steps)

def main():
	userInput = input("Check Collatz Conjecture with a number:" )
	conjecture(userInput)

main()
