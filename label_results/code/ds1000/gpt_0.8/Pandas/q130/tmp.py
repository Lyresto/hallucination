import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd

df = pd.DataFrame(data=[[1,2],[3,4],[1,2],[1,4],[1,2]],columns=['col1','col2'])

# Identify the first occurrence of each duplicate group
first_duplicates = df.duplicated(subset=['col1','col2'], keep='first')

# Get the index of the first occurrence in each group
first_duplicates_index = df.groupby(['col1','col2']).apply(lambda x: x.index[0])

# Merge the index information back into the original dataframe
df['index_original'] = df.index.isin(first_duplicates_index).astype(int)

print(df)



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)