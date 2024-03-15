import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a, index = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
result = np.zeros(np.max(index)+1)
for i in range(np.max(index)+1):
    result[i] = np.max(a[index==i])

#print(result)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
