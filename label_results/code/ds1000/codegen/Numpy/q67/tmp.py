import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a, b = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
a = np.random.rand(3, 3, 3)
b = np.arange(3*3*3).reshape((3, 3, 3))

#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
