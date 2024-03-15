def load_data():
	# your code
	df = pd.read_csv("/Users/karavi/Downloads/WATER_COACH.csv")
	transform = csr_matrix((dict(zip(df.columns,df.values)),(df.columns,df.values)),shape=(len(df.columns),len(df.values)))
	return df, transform
