import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a, col, multiply_number = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
col_array = a[:, col] * multiply_number
cumulative_sum = np.cumsum(col_array)
result = cumulative_sum

#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
