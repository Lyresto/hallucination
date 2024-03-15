import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
x, y = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
x = [[2, 2, 2],
     [2, 2, 2],
     [2, 2, 2]]
y = [[3, 3, 3],
     [3, 3, 3],
     [3, 3, 1]]
z = np.array(x)
z = np.array(y)
z = np.array(z)

#print(z)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(z, file)
