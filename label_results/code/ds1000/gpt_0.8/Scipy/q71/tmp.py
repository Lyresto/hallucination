
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import numpy as np
from scipy.spatial import distance
shape = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
from scipy.spatial import distance




def get_distance_2(y, x):
    mid = np.array([[shape[1]/2, shape[0]/2]]) # center point
    points = np.dstack((y, x))
    distances = distance.cdist(points, mid)
    return distances

y, x = np.indices(shape)
result = get_distance_2(y, x)
print(result)



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
