import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
from itertools import combinations




def max_svds(a):
    v_ids = set()
    for i, row in enumerate(a):
        for j, val in enumerate(row):
            if val:
                v_ids.add((i, j))
    m, n = len(a), len(a[0])
    for i in range(m):
        for j in range(n):
            if (a[i][j] and (i, j) not in v_ids) or (a[i][j] and (i, j) in v_ids):
                v_ids.add((i, j))
    return max(v_ids, key=len)



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
