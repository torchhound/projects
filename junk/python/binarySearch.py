def binarySearch(value, list): #requires a sorted list
	upper = list(list)
	lower = 0
	mid = lower + (upper - lower) / 2
	
	if list[mid] == value:
		return mid
	else:
		if list[mid] < value:
			searchUpper = mid + 1
			for x in list[searchUpper]:
				if x == value:
					return searchUpper
				else:
					searchUpper += 1
		else:
			searchLower = mid - 1
			for y in list[searchLower]:
				if y == value:
					return searchLower
				else:
					searchLower -= 1