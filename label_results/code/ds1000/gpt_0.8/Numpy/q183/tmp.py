import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
c, CNTS = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np

c = np.array([[[ np.nan, 763]],
              [[ 57, 763]],
              [[ 57, 749]],
              [[ 75, 749]]])

CNTS = [np.array([[[  np.nan, 1202]],
                  [[  63, 1202]],
                  [[  63, 1187]],
                  [[  78, 1187]]]),
        np.array([[[ 75, 763]],
                  [[ 57, 763]],
                  [[ np.nan, 749]],
                  [[ 75, 749]]]),
        np.array([[[ 72, 742]],
                  [[ 58, 742]],
                  [[ 57, 741]],
                  [[ 57, np.nan]],
                  [[ 58, 726]],
                  [[ 72, 726]]]),
        np.array([[[ np.nan, 194]],
                  [[ 51, 194]],
                  [[ 51, 179]],
                  [[ 66, 179]]])]

result = any(np.array_equal(c, arr) for arr in CNTS)
print(result)



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
