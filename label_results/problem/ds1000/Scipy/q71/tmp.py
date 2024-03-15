
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import numpy as np
from scipy.spatial import distance
shape = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
mid = np.array([(shape[0]-1)/2, (shape[1]-1)/2])
y, x = np.indices(shape)
coords = np.column_stack((y.ravel(), x.ravel()))
result = distance.cdist(coords, [mid])
result = result.reshape(shape)

#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
