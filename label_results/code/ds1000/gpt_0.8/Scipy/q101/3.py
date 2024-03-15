import scipy.optimize as sciopt
import numpy as np
import pandas as pd

# Define the multinomial log-likelihood function
def multinomial_loglikelihood(weights, frequencies):
    n = np.sum(frequencies) # total number of observations
    k = len(weights) # number of categories
    log_likelihood = 0
    
    for i in range(k):
        log_likelihood += frequencies[i] * np.log(weights[i])
    
    log_likelihood -= n * np.log(np.sum(weights))
    
    return -log_likelihood

# Define the constraints for the optimization problem
def constraint(weights):
    return np.sum(weights) - 1

# Set the initial guess for the weights
initial_weights = np.ones(len(a['A1'])) / len(a['A1'])

# Set the bounds for the weights
bounds = [(0, 1)] * len(a['A1'])

# Perform the optimization
result = sciopt.minimize(multinomial_loglikelihood, initial_weights, args=(a['A1'],), method='SLSQP', constraints={'type': 'eq', 'fun': constraint}, bounds=bounds)

# Get the optimized weights
weights = result.x

# Print the optimized weights
print('Category:', list(range(len(a['A1']))))
print('Weights:', weights)
