import numpy as np
array_of_arrays = np.array([np.arange(a*b).reshape(a,b) for (a,b) in pairs])
a = array_of_arrays[:]
b = array_of_arrays[:][:]
c = np.array(array_of_arrays, copy=True)
