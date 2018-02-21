def quickSort(data): #for lists
	pivot = len(data)
	right = data[pivot - 1]
	left = data[0]
	lPointer = left
	rPointer = right
	while True:
		while left < pivot:
			lPointer -= 1
			break
		while right > pivot:
			rPointer += 1
			break
		if lPointer >= rPointer:
			break
		else:
			right, left = left, right
	return data