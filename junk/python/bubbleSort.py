def bubbleSort(list):
	listPtr = 0
	for x in list:
		if x > list[listPtr + 1]:
			list.insert(listPtr + 1, x)
		elif x == list[listPtr + 1]:
			continue
		else:
			continue 
