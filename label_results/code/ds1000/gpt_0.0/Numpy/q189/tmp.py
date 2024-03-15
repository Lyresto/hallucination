import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
x, y, a, b = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
result = np.where((x == a) & (y == b))[0][0] if np.sum((x == a) & (y == b)) > 0 else -1

#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
