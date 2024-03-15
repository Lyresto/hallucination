import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

def f(dict, df):
    ### BEGIN SOLUTION

    result = df.replace(dict, inplace=False)
    ### END SOLUTION
    return result

f(example_dict, example_df)

    ### END SOLUTION


dict, df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
result = f(dict, df)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)