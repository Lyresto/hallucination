import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix

df_origin, transform_output = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION



def load_data():
    # your code
    df = pd.read_csv("/Users/karavi/Downloads/WATER_COACH.csv")
    transform = csr_matrix((dict(zip(df.columns,df.values)),(df.columns,df.values)),shape=(len(df.columns),len(df.values)))
    return df, transform



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(df, f)
