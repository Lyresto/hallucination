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
df = pd.DataFrame({'cokey':[11168155,11168155,11168155,11168156,11168156],
                   'A':[18,0,56,96,0],
                   'B':[56,18,96,152,96]})

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)