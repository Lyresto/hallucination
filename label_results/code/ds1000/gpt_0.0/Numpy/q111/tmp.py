import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
dims, a, index = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
result = np.ravel_multi_index(index, dims, order='F') + 1

#print(result)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
