import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
arr, n1, n2 = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
n1 = [1,2,3,4,5]
n2 = [6,7,8,9,10]
arr = (np.random.rand(5,50)-0.5) * 50

for i in range(0,len(n1)):
    temp_arr = arr.copy()
    mask = temp_arr < n1[i]
    temp_arr[mask] = 0
    arr[temp_arr] = arr[temp_arr] + 5

for i in range(0,len(n2)):
    temp_arr = arr.copy()
    mask = temp_arr < n2[i]
    temp_arr[mask] = 0
    arr[temp_arr] = arr[temp_arr] + 5



#print(arr)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(arr, file)
