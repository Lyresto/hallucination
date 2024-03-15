import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
A, ncol = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
A = np.array([1,2,3,4,5,6])
ncol = 2
B = vec2matrix(A,ncol=ncol)

#print(B)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(B, file)
