import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf

x = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def f(x):
    ### BEGIN SOLUTION



def f(x=example_x):
    decode_x = lambda bytes_: [decode(s) for s in bytes_]
    return decode_x(x)




def decode(s):
    return s.decode('utf-8')



    ### END SOLUTION
result = f(x)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)