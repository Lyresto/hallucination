import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def mask(a):
    a_min = np.min(a, axis=1)
    return np.array([[i[axis] for i in a] for axis in range(a.shape[1])])[a_min == 0]



#print(mask)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(mask, file)
