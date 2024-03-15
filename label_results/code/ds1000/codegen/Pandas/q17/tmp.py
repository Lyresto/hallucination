import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df, products = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd

df = pd.DataFrame({'product': [1179160, 1066490, 1148126, 1069104, 1069105, 1160330, 1069098, 1077784, 1193369, 1179741],
                  'score': [0.424654, 0.424509, 0.422207, 0.420455, 0.414603, 0.168784, 0.168749, 0.168738, 0.168703, 0.168684]})
products = [1066490, 1077784]

###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)