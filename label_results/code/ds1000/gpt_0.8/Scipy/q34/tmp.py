
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import numpy as np
from scipy.sparse import csr_matrix

col = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
mean = col.mean()
standard_deviation = col.std()



#print(mean)
#print(standard_deviation)



with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump([mean, standard_deviation], f)
