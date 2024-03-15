import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np
data, name = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import pandas as pd
import numpy as np
data = {'D':[2015,2015,2015,2015,2016,2016,2016,2017,2017,2017], 'Q':np.arange(10)}
name= 'Q_cum'
df =... # put solution in this variable
df[name] = np.cumsum(df.Q)

#print(df)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(df, file)
