def vowel(string):
	count = 0
	vowels = {'a', 'e', 'i', 'o', 'u'}
	for x in string:
		if x in vowels:
			count += 1
			print(count)
		else:
			print("Not a vowel!")

def main():
	userInput = input("Please enter a string with vowels to be counted:" )
	vowel(userInput)

main()
