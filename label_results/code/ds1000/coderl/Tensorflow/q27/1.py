import tensorflow as tf
def f(x=example_x,y=example_y,z=example_z):
	# return the solution in this function
	# result = f(x,y,z)
	m = x[y,z]
	result = tf.matmul(x,m)
	result = result.eval()
	return result
