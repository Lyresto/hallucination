import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df_a, df_b = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd

df_a = pd.DataFrame({'EntityNum':[1001.01,1002.02,1003.03],'foo':[100,50,200]})
df_b = pd.DataFrame({'EntityNum':[1001.01,1002.02,1003.03],'a_col':['alice','bob','777'],'b_col':[7,8,9]})

result = pd.merge(df_a[['EntityNum', 'foo']], df_b[['EntityNum', 'a_col']], on='EntityNum')



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)