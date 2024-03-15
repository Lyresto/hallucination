
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
result = scipy.spatial.distance.cdist(centroids, data, 'euclidean')

#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
