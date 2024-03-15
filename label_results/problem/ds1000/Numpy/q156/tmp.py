import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
from scipy.stats import rankdata
a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
def f(a):
    ranked = rankdata(a)
    max_rank = len(ranked)
    return max_rank - ranked + 1
    ### END SOLUTION
result = f(a)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)