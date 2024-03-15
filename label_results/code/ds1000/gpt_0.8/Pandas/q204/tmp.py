import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np




def f(df):
    ### BEGIN SOLUTION
    import pandas as pd
    
    example_df = pd.DataFrame({'Name': ['Name1', 'Name2', 'Name3'],
                       '2001': [2, 1, 0],
                       '2002': [5, 4, 5],
                       '2003': [0, 2, 0],
                       '2004': [0, 0, 0],
                       '2005': [4, 4, 0],
                       '2006': [6, 0, 2]})
    
    


def f(df=example_df):
    # Calculate the cumulative average while ignoring zero values
    df = df.set_index('Name')
    df = df.mask(df == 0).cumsum(axis=1).div(df.mask(df == 0).notnull().cumsum(axis=1), axis=0)

    return df.reset_index()

result = f(example_df)
print(result)



    ### END SOLUTION


df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
result = f(df)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)