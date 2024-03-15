import numpy as np
from sklearn.preprocessing import MinMaxScaler
np_array = load_data()

def Transform(a):
	# return the solution in this function
	# new_a = Transform(a)
	# ### BEGIN SOLUTION
	scaler = MinMaxScaler()
	return np.array([scaler.transform(np_array[:,i]) for i in range(len(np_array[:,0]))])
