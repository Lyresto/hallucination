import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

def f(df):
    ### BEGIN SOLUTION
    # Create a copy of the original dataframe
        df_copy = df.copy()
        
        # Replace all 0 values with NaN
        df_copy = df_copy.replace(0, pd.np.nan)
        
        # Calculate the cumulative sum for each row
        cum_sum = df_copy.iloc[:, 1:].cumsum(axis=1)
        
        # Count the number of non-NaN values for each row
        count = df_copy.iloc[:, 1:].count(axis=1)
        
        # Calculate the cumulative average for each row
        cum_avg = cum_sum.div(count, axis=0)
        
        # Replace all NaN values with 0
        cum_avg = cum_avg.fillna(0)
        
        # Add the Name column back to the dataframe
        cum_avg.insert(0, 'Name', df['Name'])
        
        return cum_avg
    ### END SOLUTION
    ### END SOLUTION


df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
result = f(df)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)