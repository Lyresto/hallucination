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
df = pd.DataFrame({
'group': ['A', 'A', 'A', 'B', 'B'],
'group_color' : ['green', 'green', 'green', 'blue', 'blue'],
'val1': [5, 2, 3, 4, 5], 
'val2' : [4, 2, 8, 5, 7]
})
  group group_color  val1  val2
group                        
A           green    10    14
B            blue     9    12

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)