
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import scipy.integrate
c, low, high = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def f(c=5, low=0, high=1):
    import scipy.integrate
    
    


def f(c, low, high):
    results = []
    for i in range(len(c)):
        eqn = lambda x: 2 * c[i] * x
        result, error = scipy.integrate.quad(eqn, low, high)
        results.append(result)
    return results

c = [1, 2, 3, 4, 5]
low = 0
high = 1
solution = f(c, low, high)
print(solution)



result = f(c, low, high)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
