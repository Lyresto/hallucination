def pd_average(df):
	return (df.groupby('Name')['2005'].mean() +
			df.groupby('Name')['2006'].mean()) / 4
