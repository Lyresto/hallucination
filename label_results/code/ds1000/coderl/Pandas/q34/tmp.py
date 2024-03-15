import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd




def val_columns_generator(n):
    


def generator():
    for i in range(n):
        yield i, i+1
return generator()




def sum_columns(df, n):
    return sum(df[col].sum() for col in val_columns_generator(n))

df = pd.DataFrame({'group': ['A', 'A', 'A', 'B', 'B'], 'group_color' : ['green', 'green', 'green', 'blue', 'blue'], 'val1': [5, 2, 3, 4, 5], 'val2' : [4, 2, 8, 5, 7], 'val3': [1,1,4,5,1], 'val4': [2,2,3,4,5]})
print((sum_columns(df, 3)))



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)