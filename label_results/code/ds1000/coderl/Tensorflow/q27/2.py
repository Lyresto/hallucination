import numpy as np
def f(x=example_x,y=example_y,z=example_z):
	# return the solution in this function
	# result = f(x,y,z)
	x_np = np.array(x)
	y_np = np.array(y)
	z_np = np.array(z)
	m = x_np[y_np,z_np]
	return m.tolist()
