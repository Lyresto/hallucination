import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

a,b,c = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import numpy as np
import pandas as pd




def cycle(df):
    it = iter(df.iterrows())
    return list(zip(*(next(it) for _ in range(len(df.columns)))))


# print(cycle(a))
# print(cycle(b))
# print(cycle(c))



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)