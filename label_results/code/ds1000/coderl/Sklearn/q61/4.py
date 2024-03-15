def solve(features):
	df = pd.DataFrame.from_records(zip(*features))
	clf = sklearn.OneHotEncoder(int)
	return clf.transform(df.loc[:,'f1'].values).tolist()
