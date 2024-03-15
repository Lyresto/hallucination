import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
r_old = r
r_new = r

#print(r_old, r_new)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump([r_old, r_new], file)
