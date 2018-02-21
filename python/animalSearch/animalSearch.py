def animalSearch(name):
	f = open("animals.txt", "r")
	count = 0
	try:
		for x in f:
			if name in x:
				count += 1
				print(x + " " + str(count))
	finally:
		f.close()
			
def main():
	i = input("Enter name to find in an animal's common name: ")
	animalSearch(i)
	roommates = ["hannah", "sam", "milo", "tristan", "marie", "melissa", "andy", "gabe", "heather", "sydny", "stephan", "courtney", "brett", "juan", "alex", "anthony", "whitney", "anne", "gina", "joey"]
	for y in roommates:
		print(y)
		animalSearch(y)
	
if __name__ == "__main__":
	main()