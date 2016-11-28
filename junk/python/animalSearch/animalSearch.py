def animalSearch(name):
	f = open("animals.txt", "r")
	for x in f:
		if name in x:
			print(x)
			
def main():
	i = input("Enter name to find in an animal's common name: ")
	animalSearch(i)
	
if __name__ == "__main__":
	main()