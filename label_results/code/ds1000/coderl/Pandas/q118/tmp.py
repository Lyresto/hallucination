import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np
import io

df, test = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd
import re




def select(df, rows):
    print(rows)
    for row in df.index.values:
        print(row)
    rows = [row.replace('rs', '').replace(':', '') for row in rows]
    print(rows)
    return df.select(rows)



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)