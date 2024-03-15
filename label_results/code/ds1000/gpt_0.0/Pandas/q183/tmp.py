import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

def f(dict, df):
    ### BEGIN SOLUTION
    # Use map to apply the values from the dict to the 'Member' column in the DataFrame
    df['Date'] = df['Member'].map(dict)
    
    # Use fillna to replace any NaN values with the original values in the 'Member' column
    df['Date'] = df['Date'].fillna(df['Member'])
    
    # Drop the 'Member' column since it's no longer needed
    df = df.drop('Member', axis=1)
    
    # Return the updated DataFrame
    return df
    ### END SOLUTION
    ### END SOLUTION


dict, df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
result = f(dict, df)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)