import numpy as np
import scipy.interpolate

array = np.random.randint(0, 9, size=(10, 10, 10))
x = np.linspace(0, 10, 10)
x_new = np.linspace(0, 10, 100)

# Reshape the array to have a single dimension
reshaped_array = array.reshape(-1, array.shape[-1])

# Create a 1D interpolation function
f = scipy.interpolate.interp1d(x, reshaped_array, axis=0)

# Interpolate the values at the new x points
new_array = f(x_new)

# Reshape the new array to match the original shape
new_array = new_array.reshape((len(x_new),) + array.shape[1:])

new_array