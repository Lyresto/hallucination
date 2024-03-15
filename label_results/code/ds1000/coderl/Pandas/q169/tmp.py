import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import numpy as np
from pandas import DataFrame




def __starting_point():
    df = DataFrame({'A': [1,1,0,1], 'B': [0,0,0,0], 'C': [1,1,0,1], 'D': [0,1,0,1]})
    ans = np.array([['0','1','1','0'],[0,'1','1','1'],[0,'1','0','0'],[1,1,1,1]])
    print(ans)
    print(df)
    print(df.sum(0))

__starting_point()



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)