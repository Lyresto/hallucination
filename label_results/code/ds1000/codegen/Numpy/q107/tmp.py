import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import pandas as pd
A, a, b = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
import pandas as pd
A = pd.Series(np.random.randn(10,))
a = 2
b = 3
BEGIN SOLUTION

#print(B)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(B, file)
