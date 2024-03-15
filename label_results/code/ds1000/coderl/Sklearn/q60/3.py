def pick_features(features):
	new_arr = []
	for sample, arr in enumerate(features):
		new_arr.append([0]*len(sample))
		for i in range(len(sample)):
			if arr[i] == 0:
				new_arr[i][sample[i]] = 1
	return np.array(new_arr)
