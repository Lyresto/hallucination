import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
arr, n1, n2 = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
arr_temp = arr.copy()
for i in range(arr.shape[0]):
    mask1 = arr_temp[i] < n1[i]
    mask2 = arr_temp[i] >= n2[i]
    mask3 = ~(mask1 | mask2)
    arr[i][mask1] = 0
    arr[i][mask2] = 30
    arr[i][mask3] += 5

#print(arr)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(arr, file)
