import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np

numerator, denominator = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
from fractions import Fraction



def reduce_fractions(numerator,denominator):
    f = Fraction(numerator,denominator)
    if f.numerator == 0 or f.denominator == 0:
        return (float("NaN"),float("NaN"))
    elif f.numerator % f.denominator == 0:
        ans = (f.numerator,f.denominator)
    else:
        ans = (f.numerator//f.denominator,f.denominator//f.numerator)
    return ans



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
