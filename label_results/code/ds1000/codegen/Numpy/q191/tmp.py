import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
x, y = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
x = [-1, 2, 5, 100]
y = [123, 456, 789, 1255]
result = np.linalg.norm(x - y, ord=2)

#print(result)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
