import scipy.spatial
centroids = np.array(list(zip(*list(zip(*np.random.rand(5, 3))))))
result = []
for i in range(5):
	root = scipy.spatial.Cubic(centroids[i:], data[i:])
	p = scipy.cluster.hierarchy.cut_tree(root, leaf_size=1)
	result.append(p[0][0][0])
