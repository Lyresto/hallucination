import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import scipy.stats
a, b = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
import scipy.stats
a,b=np.mean(a),np.mean(b)
c=np.array([sum(np.random.randn(i)) for i in range(40)]).T
d=np.array([sum(np.random.randn(i)) for i in range(50)]).T
p_value=scipy.stats.t.ppf(c,d)[2]



#print(p_value)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(p_value, file)
