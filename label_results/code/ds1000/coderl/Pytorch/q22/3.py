def get_mask(lens):
	#your code here
	mask = [[0] * len(lens) for _ in range(len(lens))]
	for i in range(len(lens)):
		for j in range(len(lens)):
			if i == j:
				mask[i][j] = 1
			else:
				mask[i][j] = 1 if lens[i + 1] - lens[j + 1] == 1 else 0
	return mask
