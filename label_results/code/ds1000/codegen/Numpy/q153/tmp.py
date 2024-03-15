import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
A, B = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
A = np.array([1,1,2,3,3,3,4,5,6,7,8,8])
B = np.array([1,4,8])
C =... # put solution in this variable
END SOLUTION
"""

"""
## Problem 2
"""

"""
I have two arrays A (len of 3.8million) and B (len of 3). For the minimal example, lets take this case:
A = np.array([1,1,2,3,3,3,4,5,6,7,8,8])
B = np.array([1,4,8])       #
#print(C)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(C, file)
