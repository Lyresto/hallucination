import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
import sklearn

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION
import pandas as pd




def one_hot(col):
    seen = set()
    return [1 if col[i] in seen else 0 for i in range(len(col))]




def load_data():
    return pd.DataFrame(one_hot(df[col] for col in df.columns), columns=df.columns)



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(df_out, f)
