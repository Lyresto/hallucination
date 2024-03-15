import numpy as np
import scipy.spatial
centroids = np.random.rand(5, 3)
data = np.random.rand(100, 3)
result = scipy.spatial.distance.cdist(centroids, data, 'euclidean')
