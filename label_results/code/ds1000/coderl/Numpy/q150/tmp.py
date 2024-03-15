import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a, number = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np




def is_contained(a):
    if len(a) == 0:
        return False
    elif len(a) == 1:
        if a[0] == 0:
            return False
        else:
            return True
    else:
        for n in range(len(a)):
            if a[n] == 0:
                return False
            elif n > 1:
                if a[n - 1] == 0:
                    return False
        return True



#print(is_contained)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(is_contained, file)
