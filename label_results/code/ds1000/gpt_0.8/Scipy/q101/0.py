First, we need to define the likelihood function for the multinomial distribution. The likelihood function represents the probability of obtaining the observed data given the parameters of the distribution.

In the multinomial distribution, the likelihood function is given by:

L(p1, p2, ..., pn) = (n! / (x1! * x2! * ... * xn!)) * (p1^x1) * (p2^x2) * ... * (pn^xn)

where n is the total number of observations, xi is the frequency of category i, and pi is the probability of category i.

To find the maximum likelihood estimate (MLE) of the parameters (probabilities) of the multinomial distribution, we need to maximize the likelihood function. This can be done by minimizing the negative log-likelihood function, which is mathematically equivalent.

In Python, we can use the `scipy.optimize.minimize` function to find the minimum of a function. We will define a negative log-likelihood function, which takes the parameters as input and returns the negative log-likelihood value.

Here is the code to estimate the parameters of the multinomial distribution using maximum likelihood estimation:

```python
import scipy.optimize as sciopt
import numpy as np
import pandas as pd

def multinomial_negative_log_likelihood(params, frequencies):
    n = np.sum(frequencies)
    log_likelihood = np.sum(frequencies * np.log(params))
    return -log_likelihood

a = pd.DataFrame({'A1':[0,1,2,3,2,1,6,0,1,1,7,10]})
frequencies = a['A1'].values

# Initial guess for the parameters
params_initial = np.ones(len(np.unique(frequencies))) / len(np.unique(frequencies))

# Define the bounds for the parameters (probabilities should be between 0 and 1)
bounds = [(0, 1)] * len(params_initial)

# Minimize the negative log-likelihood function
result = sciopt.minimize(multinomial_negative_log_likelihood, params_initial, args=(frequencies,), bounds=bounds)

# Extract the estimated parameters
weights = result.x

print("Estimated parameters:")
for i, weight in enumerate(weights):
    print(f"Category {i}: {weight:.3f}")
```

The code above uses the `scipy.optimize.minimize` function to find the minimum of the negative log-likelihood function. We specify the initial guess for the parameters (`params_initial`), the observed frequencies (`frequencies`), and the bounds for the parameters (`bounds`). The result of the optimization is stored in the `result` variable. We extract the estimated parameters (`weights`) from the result and print them.

Note that the bounds for the parameters are set to (0, 1) to ensure that the estimated probabilities are valid (between 0 and 1).

Hope this helps! Let me know if you have any further questions.