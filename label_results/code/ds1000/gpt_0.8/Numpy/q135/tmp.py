import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a, m = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
result = np.unpackbits(np.uint8(a.reshape(-1,1)), axis=1)[:, -m:]



#print(result)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
