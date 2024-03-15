import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a, b = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
a = np.array( # dims: 3x3x2
    [[[ 0,  1],
     [ 2,  3],
     [ 4,  5]],
    [[ 6,  7],
     [ 8,  9],
     [10, 11]],
    [[12, 13],
     [14, 15],
     [16, 17]]]
)
b = np.array( # dims: 3x3
    [[1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]]
)
#
#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
