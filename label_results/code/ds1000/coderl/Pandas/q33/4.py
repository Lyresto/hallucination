from pandas import mean

# First attempt
def find_mean(df, col_name):
	if col_name in df:
		val = df[col_name]
		return mean(val)
	else:
		return None

# Second attempt
def find_mean_of_each_value(df, col_name):
	val_list = df[col_name]
	mean_list = [mean(val_list) for val in val_list]
	return mean(mean_list)
