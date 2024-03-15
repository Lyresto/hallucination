import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
size, one_ratio = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
# Calculate the number of ones and zeros based on the given ratio
num_ones = int(one_ratio * size)
num_zeros = size - num_ones

# Create an array with the specified number of ones and zeros
ones = np.ones(num_ones)
zeros = np.zeros(num_zeros)

# Concatenate the arrays to get the final random array
nums = np.concatenate((ones, zeros))

# Shuffle the array to ensure randomness
np.random.shuffle(nums)



#print(nums)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(nums, file)
