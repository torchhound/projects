def pullIndex(lst):
	print("pullIndex:")
	for x in lst:
		print(x, lst.index(x))

def enumIndex(lst):
	print("enumIndex:")
	for x, value in enumerate(lst, 0):
		print(x, value)

def main():
	test1 = [1,2,3,4,5,6,7,8,9]
	test2 = [0,1,2,3,4,5,6,7,8,9]
	pullIndex(test1)
	enumIndex(test1)
	pullIndex(test2)
	enumIndex(test2)

if __name__ == "__main__":
	main()
