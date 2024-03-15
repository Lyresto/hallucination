from sklearn.preprocessing import MinMaxScaler
def Transform(a):
	# return the solution in this function
	# new_a = Transform(a)
	# ### BEGIN SOLUTION
	scaler = MinMaxScaler()
	return np.array([scaler.fit_transform(x).tolist()[i] for i, x in enumerate(a)])
