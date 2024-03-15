import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df, columns = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION
import numpy as np




def df_select_rows_to_numpy(df):
    num_rows = len(df)
    num_columns = len(df.columns)
    training_set = np.full((num_rows, num_columns), -np.inf)
    for row, col in zip(df.itertuples(), df.columns.itertuples()):
        if row[col].min() > 0.45:
            training_set[row] = row[col]
    return training_set



### END SOLUTION
print(result)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)