import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
c, CNTS = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
# 


def test_remove_contour(c):
#     print(c in CNTS)
#     print(c in CNTS[0])
#     return True

# 


def test_remove_contour(c):
#     print(c in CNTS)
#     print(c in CNTS[0])
#     return True

    import numpy as np
    
    


def test_is_contour_member(c, CNTS):
    print(c in CNTS)
    print(c in CNTS[0])
    return np.all(c in CNTS)



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
