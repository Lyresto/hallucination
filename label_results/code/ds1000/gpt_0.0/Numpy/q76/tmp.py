import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
pairs, array_of_arrays = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))

import copy
for arr in array_of_arrays:
    print(arr)
copy.deepcopy(array_of_arrays)
result = np.array([copy.deepcopy(arr) for arr in array_of_arrays])



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
