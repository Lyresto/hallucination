import scipy.spatial
example_arr = np.array([[0, 0, 0, 2, 2, 0, 0, 0, 0, 0],
                          [0, 0, 2, 0, 2, 2, 0, 6, 0, 3, 3, 3],
                          [0, 0, 0, 0, 2, 2, 0, 0, 3, 3, 3],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 1, 0, 0, 0, 0, 3, 3, 3, 0, 0],
                          [1, 1, 1, 0, 0, 0, 3, 3, 3, 0, 0],
                          [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 4]])
distances = []
def find_distances(example_array, start, end):
	for i in range(start, end+1):
		for j in range(start, end+1):
			distances.append(example_array[i][j]**2)
distances.sort()
def plot_distances(example_array, start, end):
	for i in range(start, end+1):
		example_array[i][end] = distances[i]
		plt.imshow(example_array, cmap="spectral", interpolation='nearest')
