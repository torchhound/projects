def enumZip(lst):
	for i, value in enumerate(lst, 0):
		print(zip(list(i), list(value)))

def main():
	enumZip([1,2,3,4,5,6,7,8,9])
	enumZip(["a", "b", "c", "d"])

if __name__ == "__main__":
	main()
