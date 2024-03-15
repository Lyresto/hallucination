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
df_transformed = pd.DataFrame(transform_output.toarray())
df = pd.concat([df_origin, df_transformed], axis=1)



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(df, f)
