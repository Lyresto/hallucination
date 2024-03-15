import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df, filter_list = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd



def query_dataframe(df, filter_list):
    result = df.copy()
    for i in range(len(filter_list)):
        if filter_list[i] == 'Foo':
            result = result.loc[result['Index']!= i, 'Index']
        if filter_list[i] == 'Bar':
            result = result.loc[result['Index']!= i, 'Category']
    return result



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)