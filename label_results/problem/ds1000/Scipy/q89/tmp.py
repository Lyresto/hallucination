
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
from scipy import sparse
import numpy as np
import math
sa = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
#iterate through columns
for Col in range(sa.shape[1]):
    Column = sa[:,Col].data
    List = [x**2 for x in Column]
    #get the column length
    Len = math.sqrt(sum(List))
    #normalize column
    sa[:,Col] = (1/Len)*Column
END SOLUTION

#print(sa)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(sa, f)
