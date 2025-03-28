
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import scipy.integrate
c, low, high = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
def f(c=5, low=0, high=1):

    result = scipy.integrate.quad(lambda x: c*x,low,high)
    ### END SOLUTION
    return result


result = f(c, low, high)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
