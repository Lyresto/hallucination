import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
A, NA = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
NA = np.asarray(A)
print((np.mean(NA, axis=0)))



#print(AVG)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(AVG, file)
