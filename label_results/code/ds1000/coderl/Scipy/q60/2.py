from scipy.interpolate import interp1d
import numpy as np
new_array = np.zeros((1000, 100, 100))
x = np.arange(0, 100, 1)
x_new = np.arange(0, 100, 0.1)
for i in x:
	for j in x:
		f = interp1d(x, array[:, i, j])
		new_array[:, i, j] = f(x_new)
print(new_array)
