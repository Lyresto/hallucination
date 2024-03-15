import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
arr, n1, n2 = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
arr = (np.random.rand(5, 50)-0.5) * 50
n1 = [1,2,3,4,5]
n2 = [6,7,8,9,10]

mask1 = arr < np.array(n1)[:, np.newaxis]
mask2 = arr >= np.array(n2)[:, np.newaxis]
mask3 = mask1 ^ mask2

arr[mask1] = 0
arr[mask2] = 30
arr[mask3] += 5



#print(arr)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(arr, file)
