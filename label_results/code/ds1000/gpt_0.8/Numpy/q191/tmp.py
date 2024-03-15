import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
x, y = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np

# Define the function to approximate



def f(x, a, b, c):
    return a * x ** 2 + b * x + c

# Define the error function



def error(params):
    a, b, c = params
    return np.sum((f(x, a, b, c) - y) ** 2)

# Initial guess for the parameters
initial_guess = [1, 1, 1]

# Minimize the error function
result = minimize(error, initial_guess)

result.x


#print(result)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
