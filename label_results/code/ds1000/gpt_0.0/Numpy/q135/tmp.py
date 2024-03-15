import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a, m = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
def int_to_bin_array(num, m):
    if num < 0:
        num = 2**m + num
    bin_str = bin(num)[2:]
    bin_arr = np.zeros(m, dtype=int)
    for i in range(len(bin_str)):
        bin_arr[m-len(bin_str)+i] = int(bin_str[i])
    return bin_arr

result = np.zeros((len(a), m), dtype=int)
for i in range(len(a)):
    result[i] = int_to_bin_array(a[i], m)



#print(result)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
