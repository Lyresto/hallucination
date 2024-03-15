
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import scipy.spatial
import numpy as np

centroids, data = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))

import numpy as np
from scipy.spatial.distance import cdist

# Calculate the distance between each data point and each centroid
distances = cdist(data, centroids)

# Find the index of the closest data point for each centroid
closest_indices = np.argmin(distances, axis=0)

result = closest_indices



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
