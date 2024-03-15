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


strs = ['Stackoverflow_1234',
        'Stack_Over_Flow_1234',
        'Stackoverflow',
        'Stack_Overflow_1234']
df = pd.DataFrame(data={'SOURCE_NAME': strs})

###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)