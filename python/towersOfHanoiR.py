def moveDisks(tA, tB, tC):
	def mv(x, y): x.append(y.pop(0))
	def push(x, y): x.insert(0, y.pop(0))
	while len(tA) > 1:
		mv(tB, tA)
	mv(tC, tA)
	while len(tB) != 0:
		tB.reverse()
		push(tC, tB)

def towers(disks):
	towerA = list(range(int(disks) + 1))
	towerA.remove(0)
	towerB = []
	towerC = []
	print(towerA, towerB, towerC)
	moveDisks(towerA, towerB, towerC)
	print(towerA, towerB, towerC)

def main():
	userDisk = input("How many disks?: ")
	towers(userDisk)

if __name__ == "__main__":
	main()
