import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
np.random.seed(42) # set the random seed to a fixed value
r_old = np.random.randint(3, size=(100, 2000)) - 1
r_new = np.random.randint(3, size=(100, 2000)) - 1

#print(r_old, r_new)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump([r_old, r_new], file)
