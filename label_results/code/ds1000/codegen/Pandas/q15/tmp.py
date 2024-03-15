import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
df = pd.DataFrame({'name': ['matt', 'james', 'adam'],
                  'status': ['active', 'active', 'inactive'],
                   'number': [12345, 23456, 34567],
                  'message': ['[job: , money: none, wife: none]',
                               '[group: band, wife: yes, money: 10000]',
                               '[job: none, money: none, wife: , kids: one, group: jail]']})

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)