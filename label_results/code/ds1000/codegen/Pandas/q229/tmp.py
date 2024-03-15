import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df, bins = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
df = pd.DataFrame({'username': ['john', 'john', 'john', 'john', 'jane', 'jane', 'jane', 'jane'],
                   'post_id': [1, 2, 3, 4, 7, 8, 9, 10],
                   'views': [3, 23, 44, 82, 5, 25,46, 56]})
bins = [1, 10, 25, 50, 100]
groups = df.groupby(pd.cut(df.views, bins))
groups.username.count()

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)