import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION



def drop_duplicates(df, keep='first'):
    d = {}
    for i, v in df.iterrows():
        if v['url'] in d:
            d[v['url']].append(i)
        else:
            d[v['url']] = [i]
    
    for k, v in d.items():
        v.sort()
        v = v[::-1]
        for i in range(len(v)):
            print((v[i], v[i - 1]))
    
    
    
    df2 = pd.DataFrame(df)
    df2.drop_duplicates(subset='url', keep=keep)



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)