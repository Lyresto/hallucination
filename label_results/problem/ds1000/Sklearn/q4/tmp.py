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
# Step 1: Create a set of all unique elements in the list column
unique_elements = set()
for row in df['Col3']:
    unique_elements.update(row)
    
# Step 2: Create a dictionary to map each unique element to a new column name
element_to_col = {}
for i, element in enumerate(unique_elements):
    element_to_col[element] = 'Col{}'.format(i+1)
    
# Step 3: Create a new dataframe with the one-hot-encoded columns
df_out = pd.DataFrame()
for element, col_name in element_to_col.items():
    df_out[col_name] = df['Col3'].apply(lambda x: 1 if element in x else 0)
    
# Step 4: Concatenate the original dataframe with the new one-hot-encoded dataframe
df_out = pd.concat([df[['Col1', 'Col2']], df_out], axis=1)

### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(df_out, f)
