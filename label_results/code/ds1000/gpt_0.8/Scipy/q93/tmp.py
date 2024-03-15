
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import numpy as np
import scipy.spatial
centroids, data = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
import scipy.spatial

centroids = np.random.rand(5, 3)
data = np.random.rand(100, 3)

# Calculate the distance between each data point and each centroid
distances = scipy.spatial.distance.cdist(data, centroids)

# Find the index of the closest centroid for each data point
closest_centroids = np.argmin(distances, axis=1)

# Find the closest point to each centroid
result = np.zeros(centroids.shape)
for i in range(centroids.shape[0]):
    cluster_points = data[closest_centroids == i]
    closest_point = cluster_points[np.argmin(scipy.spatial.distance.cdist(cluster_points, [centroids[i]]))]
    result[i] = closest_point



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
