import numpy as np
A = ['inf', '33.33', '33.33', '33.37']
NA = np.asarray(A)

# Convert 'inf' to a large number
NA[NA == 'inf'] = np.inf

# Convert the array elements to float
NA = NA.astype(float)

# Calculate the mean
AVG = np.mean(NA, axis=0)
