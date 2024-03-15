import numpy as np
import scipy.interpolate
array = np.random.randint(0, 9, size=(10, 10, 10))
x = np.linspace(0, 10, 10)
x_new = np.linspace(0, 10, 100)
for i in x:
    for j in x:
        f = scipy.interpolate.interp1d(x, array[:, i, j])
        new_array[:, i, j] = f(x_new)
