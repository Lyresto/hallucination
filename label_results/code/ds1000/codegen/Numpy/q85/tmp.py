import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
size, one_ratio = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
randomLabel = np.random.randint(2, size=numbers)
one_ratio = 0.9
size = 1000

#print(nums)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(nums, file)
