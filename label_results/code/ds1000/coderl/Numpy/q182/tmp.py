import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
c, CNTS = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np




def test_is_member_of_a_list_of_contours(c):
    print(c in CNTS)
    return c in CNTS



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)