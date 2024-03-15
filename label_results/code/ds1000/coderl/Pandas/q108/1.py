def timestamp_compare(df1, df2):
	return df1.loc[df1.index >= df2.index].values.tolist()
