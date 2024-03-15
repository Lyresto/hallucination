import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
result = []
for i in range(a.shape[0]-1):
    for j in range(a.shape[1]-1):
        patch = a[i:i+2, j:j+2]
        result.append(patch)
result = np.array(result)



#print(result)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
