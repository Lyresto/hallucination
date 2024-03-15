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


dates = ['2016-1-{}'.format(i)for i in range(1,21)]
values = [i for i in range(20)]
data = {'Date': dates, 'Value': values}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
ts =... # put solution in this variable

###END SOLUTION
result = ts

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)