import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd

df= pd.DataFrame({'user': ['abc','abc','efg','efg'], 'dt': ['2022-01-01','2022-01-02', '2022-01-05','2022-01-06'], 'val': [1,14,51,4]})
df['dt'] = pd.to_datetime(df['dt'])

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)