import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
# Define a function to extract key-value pairs from the message column
def extract_key_value_pairs(message):
    # Remove brackets and split by comma
    pairs = message.strip('[]').split(', ')
    # Split each pair by colon and create a dictionary
    pairs_dict = {pair.split(': ')[0]: pair.split(': ')[1] for pair in pairs}
    return pairs_dict

# Apply the function to the message column and expand the resulting dictionary into columns
df = pd.concat([df, df['message'].apply(extract_key_value_pairs).apply(pd.Series)], axis=1)

# Drop the original message column
df.drop('message', axis=1, inplace=True)

# Replace empty strings with 'none'
df.replace('', 'none', inplace=True)

# Reorder columns
df = df[['name', 'status', 'number', 'job', 'money', 'wife', 'group', 'kids']]

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)