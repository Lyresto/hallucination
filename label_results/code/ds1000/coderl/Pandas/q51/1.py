import numpy as np

def df_to_exp(df, col_name):
	exp_col_name = col_name + "_"
	exp_col_name = str(exp_col_name)
	for i, value in df.iteritems():
		try:
			exp_col_val = np.power(float(value), int(exp_col_name[1:]))
			df[col_name] = exp_col_val
		except ValueError:
			df[col_name] = [int(exp_col_name[1:])]
	return df
