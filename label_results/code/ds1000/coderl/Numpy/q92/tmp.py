import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a, N = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
a = np.array([4, 1, 0, 8, 5, 2])
N = 3



def get_result(N):
    arr = np.array(a)
    index_list = []
    for i in range(len(arr)):
        if (i == N-1):
            index_list.append(i)
        elif arr[i] > arr[i+1]:
            index_list.append(i)
    return index_list



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
