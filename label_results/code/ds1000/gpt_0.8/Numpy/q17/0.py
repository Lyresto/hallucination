import numpy as np

# Set the random seed to ensure reproducibility
np.random.seed(0)

# Generate the random array
r = np.random.randint(3, size=(100, 2000)) - 1

# Save the random array as r_old
r_old = r.copy()

# Generate a new random array using the same seed
r_new = np.random.randint(3, size=(100, 2000)) - 1

# Check if the arrays are the same
print(np.array_equal(r_old, r_new))
END SOLUTION