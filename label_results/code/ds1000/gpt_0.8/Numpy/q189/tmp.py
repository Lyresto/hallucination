import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
x, y, a, b = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
result = np.where((x == a) & (y == b))[0]
if len(result) > 0:
    result = result[0]
else:
    result = -1



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
