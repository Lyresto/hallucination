import scipy.spatial
import itertools
def distance(example_array):
	example_array = example_array.flatten()
	distances = []
	for i in range(example_array.shape[0]):
		for j in range(example_array.shape[1]):
			distances.append(min(example_array[i, j], example_array[i, j+example_array[j, 0]], example_array[i+example_array[j, 0], j+example_array[j, 1]]) + example_array[i][j])
	return distances
