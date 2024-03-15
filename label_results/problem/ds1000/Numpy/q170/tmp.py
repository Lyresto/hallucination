import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=2)
args = parser.parse_args()
import numpy as np
A, NA = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
print(NA)
# Convert strings to float values
A = [float(x) if x != 'np.inf' else np.inf for x in A]
# Calculate mean
AVG = np.mean(A)



#print(AVG)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(AVG, file)
