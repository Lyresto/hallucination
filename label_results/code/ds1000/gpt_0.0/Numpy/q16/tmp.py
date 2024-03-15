import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a, shift = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
result = np.zeros_like(a)
for i, s in enumerate(shift):
    if s > 0:
        result[i, s:] = a[i, :-s]
    elif s < 0:
        result[i, :s] = a[i, -s:]
    else:
        result[i] = a[i]
result = np.where(result == 0, np.nan, result)

#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
