'''
string[::-1]
print("".join(reversed(string)))
'''

def reverse(string):
	final = list(string)
	second = final[::-1]
	output = ""
	for x in second:
		output += x
	return output

print(reverse("cat"))
print(reverse("dog"))

