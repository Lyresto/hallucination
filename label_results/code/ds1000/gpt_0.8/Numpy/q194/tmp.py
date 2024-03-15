import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
A, B = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np

A = np.random.rand(5, 6, 3)
B = np.random.rand(3, 3)

result = np.matmul(A, B)

print(result.shape)  # shape will be (5, 6, 3)



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
