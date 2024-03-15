
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import scipy.integrate
c, low, high = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def f(c=5, low=0, high=1):
    import scipy.integrate
    


def f(c=5, low=0, high=1):
    i=0
    n=len(c)
    for n in range(n):
        eqn=2*c[n]*c[n]
        result,error=scipy.integrate.quad(lambda x: eqn,low,high)
        i+=result
    return i




result = f(c, low, high)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
