import numpy as np
def elementwise_function(element_1,element_2):
	return (element_1 + element_2)
z = [[5, 5, 5],
     [5, 5, 5],
     [5, 5, 5]]
np.add.at(0,0,z[0])
np.add.at(1,1,z[1])
np.add.at(2,2,z[2])
