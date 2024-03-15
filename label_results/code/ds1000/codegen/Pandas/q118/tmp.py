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
import io

data = io.StringIO("""
rs    alias  chrome  poston
TP3      A/C      0    3
TP7      A/T      0    7
TP12     T/A      0   12
TP15     C/A      0   15
TP18     C/T      0   18
""")
df = pd.read_csv(data, delim_whitespace=True).set_index('rs')
test = ['TP3', 'TP18']

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)