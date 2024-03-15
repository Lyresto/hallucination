import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
df = pd.DataFrame({'fips': ['00000 UNITED STATES', '01000 ALABAMA',
                           '01001 Autauga County, AL', '01003 Baldwin County, AL',
                           '01005 Barbour County, AL']})

###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)