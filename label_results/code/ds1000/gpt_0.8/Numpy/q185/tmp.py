import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np
data, name = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
df = pd.DataFrame(data)
df['Q_cum'] = df.groupby('D')['Q'].cumsum()
df


#print(df)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(df, file)
