import numpy as np
a = np.random.rand(8, 5)
col = 2
multiply_number = 5.2
result = []
for i in range(len(a)):
	multiply_result = a[:,i]*multiply_number
	result.append(np.sum(multiply_result))

