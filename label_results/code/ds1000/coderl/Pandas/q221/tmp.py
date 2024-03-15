import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION



def parse_first(s):
    try:
        while s[-1]!= '_':
            s = s[:-1]
        return s
    except:
        return s





def parse_last(s):
    try:
        while s[0]!= '_':
            s = s[1:]
        return s
    except:
        return ''



###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)