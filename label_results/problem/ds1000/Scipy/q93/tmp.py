
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import numpy as np
import scipy.spatial
centroids, data = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
result = []
for i in range(len(centroids)):
    cluster_points = data[np.where(labels == i)[0]]
    distances = scipy.spatial.distance.cdist(cluster_points, [centroids[i]])
    closest_point_idx = np.argmin(distances)
    closest_point = cluster_points[closest_point_idx]
    result.append(closest_point)

#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
