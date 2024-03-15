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
# Convert csr_matrix to a pandas DataFrame
transform_output_df = pd.DataFrame.sparse.from_spmatrix(transform_output)

# Concatenate the original DataFrame and the transformed DataFrame
df = pd.concat([df_origin, transform_output_df], axis=1)

### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(df, f)
