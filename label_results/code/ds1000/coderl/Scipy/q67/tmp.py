
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import io
from scipy import stats

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def zscore(df, x):
    # your code
    zscore = lambda x: sum(df[x].values())/len(df[x])
    return [zscore(i) for i,row in df.iterrows()]





#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
