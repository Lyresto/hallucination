import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a, pos, element = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
def f(a, pos=2, element = 66):
    a = np.insert(a, pos, element)
    return a
    ### END SOLUTION
    
    

result = f(a, pos, element)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
