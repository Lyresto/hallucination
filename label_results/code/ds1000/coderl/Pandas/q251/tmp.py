import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION



def split_dataframe(df):
    codes = df['codes']
    columns = ['code_' + str(i) for i in range(1, len(codes)+1)]
    new_df = pd.DataFrame(columns=columns)
    for i in range(len(codes)):
        values = codes[i]
        new_df['code_' + str(i)] = pd.to_numeric(values)
    new_df.fillna(value=np.nan,inplace=True)
    return new_df



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)