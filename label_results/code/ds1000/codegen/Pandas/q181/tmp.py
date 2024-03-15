import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

dict, df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd
import numpy as np

dict = {'abc':'1/2/2003', 'def':'1/5/2017', 'ghi':'4/10/2013'}
df = pd.DataFrame({'Member':['xyz', 'uvw', 'abc', 'def', 'ghi'], 'Group':['A', 'B', 'A', 'B', 'B'], 'Date':[np.nan, np.nan, np.nan, np.nan, np.nan]})

###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)