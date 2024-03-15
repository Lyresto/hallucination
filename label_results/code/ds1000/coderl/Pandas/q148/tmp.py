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
import numpy as np
d = {'l':  ['left', 'right', 'left', 'right', 'left', 'right'],
    'r': ['right', 'left', 'right', 'left', 'right', 'left'],
    'v': [-1, 1, -1, 1, -1, -1]}
df = pd.DataFrame(d)
result = df.groupby('l')['v'].sum()['right']



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)