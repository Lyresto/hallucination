
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import numpy as np
import scipy.spatial
centroids, data = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import scipy.spatial
import numpy as np




def closest_point(centroids, data):
    result = np.array([])
    for i in range(len(centroids)):
        result = np.append(result, [np.min(scipy.spatial.distance.cdist(data,centroids[i]).item())])
    return result



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
