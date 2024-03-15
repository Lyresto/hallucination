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