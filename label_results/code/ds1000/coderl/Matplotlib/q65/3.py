# 1) Panda's algorithm
# 2) Gives an idea of the function of two variables x and y, 
#    to determine the value of the k-th variable at x. 
#    We will use this to determine the value of k at x.
# 3) Using this to determine the value of k at x, we will use
#    this function to determine the value of k at y.

# SOLUTION END

def k_stat(k, x):
	# The number of x values for the k-th variable.
	n = x.size

	# The number of y-values for the k-th variable.
	m = k.size

	# The initial value for the k-th variable.
	initial = k[0,0]

	# The function to determine the value of k at x.
	def func(x):
		# y = a + b
		return initial + y

	# Function to determine the value of k at x.
	def func_2(x):
		# y = a + b
		return func(2*x)

	# Compute the value of k at y.
	def func_3(y):
		return func(3*y)

	# Compute the value of k at y.
	def func_4(y):
		return func(4*y)

	# Compute the value of k at y.
	def func_5(y):
		return func_3(y)

	# Compute the value of k at y.
	def func_6(y):
		return func_4(y)

	# Compute the value of k at y.
	def func_7(y):
		return func_5(y)

	# Compute the value of k at y.
	def func_8(y):
		return func_6(y)

	# Compute the value of k at y.
	def func_9(y):
		return func_7(y)

	# The function to call the k-th variable for x.
	def func_x(x):
		# y = a + b