import numpy as np

# np.random.uniform is a built-in function in Python. It returns n log uniform
# samples of given size (n) that suit log-uniform distribution.

def log_uniform(min, max, n):
	samples = np.random.uniform(min, max, n)
	return np.log(samples)[:n]
