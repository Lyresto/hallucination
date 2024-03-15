def raster_to_distances(example_array):
	"""
	Reads the array and returns an array of "patch ids", each of which is a distance
	between all regions in a raster patch.
	:param example_array: 2d array with shape (N, N), containing the input data
	:return: array of distance pairs as a list of (from ID, to ID, distance) pairs
	"""
	distances = []
	for i, row in enumerate(example_array):
		for j, col in enumerate(row):
			distances.append([i, j, scipy.spatial.distance.cdist(row, col)])
	return distances
