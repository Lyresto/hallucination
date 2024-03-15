import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import pandas as pd
A, a, b = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
#!/usr/bin/env python
from math import factorial as f
import numpy as np
from pandas import Series as A
a, b = [i for i in A.values()]
B = A.apply(lambda x: f(a)/(f(b)*f(a)), axis=1)



#print(B)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(B, file)
