import numpy as np
import scipy.interpolate

# def interpolate_1d(x, y, kind="linear"):
#     if kind == "linear":
#         return np.interp(x, y, kind=kind)
#     elif kind == "cubic":
#         return scipy.interpolate.spline(x, y, kind=kind)


def interpolate_daily_average(array):
	new_array = np.zeros((1000, 100, 100))
	x = np.arange(0, 100, 1)
	x_new = np.arange(0, 100, 0.1)
	for i in x:
		for j in x:
			f = interpolate_1d(x, array[:, i, j], kind="linear")
			new_array[:, i, j] = f(x_new)
	return new_array
