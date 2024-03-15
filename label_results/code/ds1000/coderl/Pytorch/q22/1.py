def get_mask(lens):
	if len(lens) == 0:
		return []
	x = []
	for i in lens:
		x.append([0]*i)
	for i in range(len(lens)):
		for j in range(i+1, len(lens)+1):
			x[i][j] = 1
	return x
