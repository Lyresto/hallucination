from pandas import groupby

def agg(df):
	result = []
	for key, group in groupby(df, key = lambda x: x[0]):
		group_list = list(group.tolist())
		result.append(list(zip(group['time'], group_list)))
	return pd.DataFrame(result)
