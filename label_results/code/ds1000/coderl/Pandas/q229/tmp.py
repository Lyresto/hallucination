import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df, bins = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
from collections import defaultdict
from itertools import groupby




def count_views_in_bins(df, bins):
    counts = defaultdict(lambda: 0)
    for u, g in groupby(df.copy(), key='post_id'):
        counts[u] += g.count()
    return sum(counts[u] for u in counts)



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)