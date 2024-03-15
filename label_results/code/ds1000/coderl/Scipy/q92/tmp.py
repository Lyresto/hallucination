
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import scipy.spatial
import numpy as np

centroids, data = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))

import scipy.spatial
import numpy as np
import itertools




def closest_to_centroid(data, centroids):
    return list(itertools.accumulate(np.searchsorted(centroids, x) for x in data))[0]



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
