
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import scipy.stats as ss
x1, x2 = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
import scipy.stats as ss
x1=[38.7,  41.5,  43.8,  44.5,  45.5,  46.0,  47.7,  58.0]
x2=[39.2,  39.3,  39.7,  41.4,  41.8,  42.9,  43.3,  45.8]
result = ss.anderson_ksamp(x1, x2)

#print(result)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
