def towersHanoi(disks):
	diskList = list(range(1, int(disks)+1))
	towerA = diskList
	towerB = []
	towerC = []
	print(diskList)
	if int(disks) % 2 == 0:
		while len(towerC) < int(disks):
			try:
				towerB = towerA.pop(0)
			except Exception:
				continue
			try:
				towerC = towerA.pop(0)
			except Exception:
				continue
			try:
				towerC = towerB.pop(0)
			except Exception:
				continue
	else:
		while len(towerC) < int(disks):
			try:
				towerC = towerA.pop(0)
			except Exception:
				continue
			try:
				towerB = towerA.pop(0)
			except Exception:
				continue
			try:
				towerB = towerC.pop(0)
			except Exception:
				continue
	return towerA, towerB, towerC

def main():
	userDisk = input("How many disks?: ")
	towersHanoi(userDisk)

if __name__ == "__main__":
	main()
