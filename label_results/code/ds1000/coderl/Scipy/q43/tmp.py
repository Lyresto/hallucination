
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import scipy.stats as ss
x1, x2 = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def anderson(x1, x2):
    p = [i/20 for i in range(len(x1))]
    a = [ss.average_difference(x1[i], x2[i]) for i in range(len(x1))]
    return (sum(a) == (len(x1)-len(x2))/2) and p == list(p)



#print(result)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
