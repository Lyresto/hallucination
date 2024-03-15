
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import scipy.spatial
import numpy as np

centroids, data = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))

result = []
for i in range(len(centroids)):
    cluster_indices = np.where(cut_tree == i)[0]
    distances = scipy.spatial.distance.cdist([centroids[i]], data[cluster_indices])
    closest_index = cluster_indices[np.argmin(distances)]
    result.append(closest_index)

#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
