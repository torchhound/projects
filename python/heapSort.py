import heapq

def heapSort(data):
	left = len(hp) #not sure if len() applies to heaps
	right = 0
	hp = heapq.heapify(data)
	for x in hp:
		if right < left:
			heapq.heapreplace(hp, hp[left])
		else:
			continue
		right += 1
		left -= 1
	return hp