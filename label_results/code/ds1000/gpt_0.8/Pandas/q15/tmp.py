import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
# Split the message column into separate key-value pairs
df['message'] = df['message'].str.strip('[]').str.replace(' ', '')
df['message'] = df['message'].str.split(',')

# Create an empty dictionary to store the key-value pairs
data_dict = {}

# Loop through each row in the dataframe
for index, row in df.iterrows():
    # Loop through each key-value pair in the message column
    for pair in row['message']:
        # Split the pair into key and value
        key, value = pair.split(':')
        # Add the key-value pair to the dictionary
        if key not in data_dict:
            data_dict[key] = []
        data_dict[key].append(value)

# Create a new dataframe from the dictionary
result = pd.DataFrame.from_dict(data_dict)

# Merge the new dataframe with the original dataframe
result = pd.merge(df, result, left_index=True, right_index=True)

# Drop the message column and rename the columns
result = result.drop('message', axis=1)
result = result.rename(columns={'job ': 'job', 'money ': 'money', 'wife ': 'wife', 'group ': 'group', 'kids ': 'kids'})

# Replace empty strings with 'none'
result = result.replace('', 'none')



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)