
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import io
from scipy import stats

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
result = df.apply(stats.zscore)

#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
