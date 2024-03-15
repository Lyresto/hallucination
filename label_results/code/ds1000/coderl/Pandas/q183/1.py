import pandas as pd
def f(dict=example_dict, df=example_df):
	# return the solution in this function
	for c in dict:
		df[c] = pd.Series(dict[c], name='Member')
	return df.fillna(df['Member'])
