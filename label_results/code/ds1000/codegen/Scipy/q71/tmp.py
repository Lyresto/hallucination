
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
shape = (6, 6)
result = np.zeros(shape)
result[0, 0] =... # put solution in this variable
result[0, 1] =... # put solution in this variable
result[1, 0] =... # put solution in this variable
result[1, 1] =... # put solution in this variable
result[2, 0] =... # put solution in this variable
result[2, 1] =... # put solution in this variable
result[3, 0] =... # put solution in this variable
result[3, 1] =... # put solution in this variable
result[4, 0] =... # put solution in this variable
result[4, 1] =... # put solution in this variable
result[5, 0] =... # put solution in this variable
result[5, 1] =... # put solution in this variable

#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
