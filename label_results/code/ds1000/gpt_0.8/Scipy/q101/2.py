# Compute the observed frequencies of each category
observed_frequencies = a['A1'].value_counts().sort_index().values

# Define the log-likelihood function for the multinomial distribution
def log_likelihood(weights, frequencies):
    n = sum(frequencies)  # Total number of observations
    p = weights / np.sum(weights)  # Normalize the weights to probabilities
    return np.sum(frequencies * np.log(p)) - n * np.log(np.sum(p))

# Define the negative log-likelihood function
def neg_log_likelihood(weights, frequencies):
    return -log_likelihood(weights, frequencies)

# Set initial weights as equal probabilities for each category
initial_weights = np.ones(len(observed_frequencies))

# Minimize the negative log-likelihood using scipy.optimize.minimize
result = sciopt.minimize(neg_log_likelihood, initial_weights, args=(observed_frequencies,))

# Extract the estimated weights from the optimization result
estimated_weights = result.x

# Normalize the weights to probabilities
probabilities = estimated_weights / np.sum(estimated_weights)

# Print the estimated probabilities
print("Category:", list(range(len(probabilities))))
print("Weights:", probabilities)
