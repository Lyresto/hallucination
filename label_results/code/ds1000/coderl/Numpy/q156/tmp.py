import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
from scipy.stats import rankdata
a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def f(a):



def f(a=example_a):
    # your code here
    d = np.array([(a.count(i),i) for i in set(a)])
    return sorted(d, reverse=True)[0][1]



result = f(a)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
