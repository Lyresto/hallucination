
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import scipy.interpolate
x, array, x_new = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
import scipy.interpolate
array = np.random.randint(0, 9, size=(10, 10, 10))
x = np.linspace(0, 10, 10)
x_new = np.linspace(0, 10, 100)
for i in x:
    for j in x:
        f = scipy.interpolate.interp1d(x, array[:, i, j])
        new_array[:, i, j] = f(x_new)

#print(new_array)



with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(new_array, f)
