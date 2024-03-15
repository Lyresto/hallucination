import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import numpy as np

df = pd.DataFrame({'a':[1,1,1,2,2,2,3,3,3], 'b':[12,13,23,22,23,24,30,35,55]})

result = df.groupby('a')['b'].agg(['mean', 'std'])
result


###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)