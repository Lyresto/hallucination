import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
size, one_ratio = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
num_ones = int(size * one_ratio)
num_zeros = size - num_ones
ones = np.ones(num_ones, dtype=int)
zeros = np.zeros(num_zeros, dtype=int)
nums = np.concatenate((ones, zeros))
np.random.shuffle(nums)



#print(nums)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(nums, file)
