import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a, shift = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
a = np.array([[ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.],
		[1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.]])
shift = [-2, 3]

#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
