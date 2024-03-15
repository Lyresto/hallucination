import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a, b = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np

a = np.array([[[ 1.,  1.,  1.],
               [ 1.,  1.,  1.],
               [ 1.,  1.,  1.]],
              
              [[ 3.,  3.,  3.],
               [ 3.,  2.,  3.],
               [ 3.,  3.,  3.]],
              
              [[ 2.,  2.,  2.],
               [ 2.,  3.,  2.],
               [ 2.,  2.,  2.]]])

b = np.array([[[ 0,  1,  2],
               [ 3,  4,  5],
               [ 6,  7,  8]],
              
              [[ 9, 10, 11],
               [12, 13, 14],
               [15, 16, 17]],
              
              [[18, 19, 20],
               [21, 22, 23],
               [24, 25, 26]]])

sum_of_a = np.sum(a, axis=(1,2))
sorted_indices = np.argsort(sum_of_a)
result = b[sorted_indices]

print(result)



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
