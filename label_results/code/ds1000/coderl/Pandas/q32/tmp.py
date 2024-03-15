import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
#try:
#    import pandas as pd
#    df = pd.DataFrame(
#        {'HeaderA': [476],
#         'HeaderB': [4365],
#         'HeaderC': [457],
#         'HeaderX': [345]})
#except ImportError:
#    pass






def rename_columns(df):
    #your code here
    new_df = df.copy()
    for i in range(len(df.columns)):
        if not any(i[-1] in ['X', 'Y'] for i in df.columns):
            new_df['Header' + i] = [i for i in df.columns if i[-1] not in ['X', 'Y']]
    return new_df



###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)