def cdist(patch):
	dist = np.zeros_like(patch)
	for i in range(len(dist)):
		for j in range(len(dist)):
			dist[i,j] = min(example_array[i,j], example_array[i,k] + example_array[k,j] for k in range(i+1,len(dist)))
	return dist
