import numpy as np

# Set a seed value for reproducibility
np.random.seed(123)

# Generate the random array
r_old = np.random.randint(3, size=(100, 2000)) - 1

# Generate a new random array using the same seed
np.random.seed(123)
r_new = np.random.randint(3, size=(100, 2000)) - 1
END SOLUTION

# Verify that r_old and r_new are the same
print(np.array_equal(r_old, r_new))  # Output: True