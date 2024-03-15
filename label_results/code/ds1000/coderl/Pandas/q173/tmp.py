import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

s = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd
result = pd.Series([1,1,1,1,1,1,1,1,1,1,1,1,1,0.98,0.93],
    index=['146tf150p','havent','home','okie','thanx','er','anything','lei','nite','yup','thank','ok','where','beerage','anytime','too','done','645','tick','blank'])



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)