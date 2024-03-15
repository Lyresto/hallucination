import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
from pandas import DataFrame
from itertools import groupby



def get_groups(df):
    print(df.groupby('text').groups)
    return df.groupby('text').groups




def merge_group(df, text):
    print(text)
    df2 = pd.DataFrame({'text': [text]})
    for key,group in groupby(df,key):
        print(key)
        print(group)
        df2['text'] += [str(group)]
    return df2




def merge_rows(df):
    text_group = get_groups(df)
    print(text_group)
    new_df = pd.DataFrame({'text':[i for (key,group) in text_group]})
    return new_df
    



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)