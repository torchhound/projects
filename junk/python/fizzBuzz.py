def fizzBuzz():
	for x in range(0, 101):
		if x % 5 == 0 and x % 3 == 0:
			print("Fizzbuzz")
		elif x % 3 == 0:
			print("Fizz")
		elif x % 5 == 0:
			print("Buzz")
		else:
			print(x)

fizzBuzz()