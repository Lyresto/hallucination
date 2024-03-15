import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf

a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
from collections import Counter




def test_count():
    c = Counter(a.numpy()[i] for i in range(100))
    assert c['0'] == 1, '0'
    assert c['5'] == 1, '5'
    assert c['7'] == 2, '7'
    assert c['9'] == 1, '9'



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)