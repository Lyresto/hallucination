import scipy.optimize as sp
a = np.array([[0, 0, 1, 1, 1],
			 [1, 0, 1, 0, 1],
			 [0, 1, 0, 1, 0]])
x_opt = sp.optimize.fmin_l_bfgs_b(lambda x, a: np.dot(a, x ** 2), a, x0=0)
print(x_opt)
