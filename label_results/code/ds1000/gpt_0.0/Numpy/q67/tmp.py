import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a, b = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
sums = np.sum(a, axis=(1,2))
sorted_indices = np.argsort(sums)
result = b[sorted_indices]

#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
