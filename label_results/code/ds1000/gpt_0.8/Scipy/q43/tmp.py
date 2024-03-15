
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import scipy.stats as ss
x1, x2 = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
result = ss.anderson_ksamp([x1, x2])


#print(result)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
