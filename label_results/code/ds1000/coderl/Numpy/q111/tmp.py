import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
dims, a, index = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np



def sub2ind(size, subscripts, i, j):
    arr = np.full((size,), float(i * size + j))
    for k, r in enumerate(subscripts):
        arr[:, k] = (i - r) * (size - k) / size
    return round(sum(arr), 8)



#print(result)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
