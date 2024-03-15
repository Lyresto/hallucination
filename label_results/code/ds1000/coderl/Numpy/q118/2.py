def elementwise_function(element_1,element_2):
	return (element_1 + element_2)
import numpy as np
x = np.array(x)
y = np.array(y)
z = np.array([elementwise_function(x[i],y[i]) for i in range(2)]).reshape(3,2)
print(z)
