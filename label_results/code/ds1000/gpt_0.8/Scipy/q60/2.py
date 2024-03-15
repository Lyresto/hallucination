import numpy as np
import scipy.interpolate

# Reshape the array to have the shape (n, m), where n is the number of samples
# and m is the number of features (in this case, 10*10)
reshaped_array = array.reshape(array.shape[0], -1)

# Initialize the new array
new_array = np.zeros((x_new.shape[0], reshaped_array.shape[1]))

# Iterate over each feature and interpolate
for i in range(reshaped_array.shape[1]):
    f = scipy.interpolate.interp1d(x, reshaped_array[:, i])
    new_array[:, i] = f(x_new)

# Reshape the new array back to the original shape
new_array = new_array.reshape(x_new.shape[0], array.shape[1], array.shape[2])

# END SOLUTION
