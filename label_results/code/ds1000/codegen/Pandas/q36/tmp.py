import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df, row_list, column_list = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd

df = pd.DataFrame({'a':[1,1,1,1],'b':[2,2,1,0],'c':[3,3,1,0],'d':[0,4,6,0],'q':[5,5,1,0]})
row_list = [0,2,3]
column_list = ['a','b','d']
result =... # put solution in this variable
END SOLUTION

df.meanAdvance(row_list,column_list,axis=0)

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)