import numpy as np
array_of_arrays = np.array([np.arange(a*b).reshape(a,b) for (a,b) in pairs])
print(array_of_arrays[:])
