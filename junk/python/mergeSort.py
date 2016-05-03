def split(data):
	half = len(data)//2
	return data[:half], data[half:]
	
def breakL(data):
	for x in data:
		if len(data) == 1:
			return data
		else:
			split(data)
			
def sort(*args):
	size = len(args)
	old = list(args)
	new = []
	for x in size:
		mx = max(old)
		mn = min(old)
		new[0] = mn
		new.append(mx)
		mxI = index(mx)
		mnI = index(mn)
		del old[mxI]
		del old[mnI]