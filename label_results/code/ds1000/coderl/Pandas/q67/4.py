def pivot_table(df, some_bool=True):
	return df.pivot(index='user', columns='01/12/15', values='value', some_bool=some_bool)
