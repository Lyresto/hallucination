import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np

min, max, n = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))

import numpy as np




def sample(n, min, max):
    return np.random.uniform(n, size=n).tolist()



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
