import numpy as np

def f(*args):
	np_args = [np.array(a) for a in args]
	sess = tf.Session()
	res = sess.run(args[0][0][0] + args[0][0][1] + args[0][1][0], 
				  args[1][0][0] + args[1][0][1], 
				  args[2][0][0] + args[2][0][1])
	return np_args[res].tolist()
