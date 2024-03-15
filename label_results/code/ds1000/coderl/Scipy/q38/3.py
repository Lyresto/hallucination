def raster_distances(example_array):
	distances = []
	for i in range(len(example_array)):
		for j in range(len(example_array)):
			distances.append(min(example_array[i][j], example_array[i][k] + example_array[k][j]))
	return distances
