from pandas import DataFrame

def extract_feature_names(df):
	df = df.drop('LOS', axis=1)
	np_df = np.array(df)
	# create array of all selected columns
	cols = np_df.shape[1] - 1
	result = [None for i in range(cols)]
	# iterate over all selected columns
	for i in range(cols):
		# run through all available columns
		np_df[:,i] = np.unique(np_df[:,i])
		# apply transform to np_df
		for k in range(cols):
			result[k] = np_df[:,k].tolist()
	return result
