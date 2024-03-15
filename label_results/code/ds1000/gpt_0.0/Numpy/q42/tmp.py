import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np

numerator, denominator = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
from fractions import Fraction

if denominator == 0:
    result = (float('nan'), float('nan'))
else:
    result = Fraction(numerator, denominator).as_integer_ratio()

result = tuple(result)

#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
