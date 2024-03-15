import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a, shift = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np




def shift(xs, shift):
    shifts = (shift[0],) + shift[1:]
    return np.roll(xs, shifts, axis=0)



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
