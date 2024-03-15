def add_timestamp(df1, df2, i, j):
	for t in range(i, j + 1):
		df2[t] += df1['data'][i]
	return df2

def match_timestamps(df1, df2):
	for i, d1 in enumerate(df1['data']):
		for j, d2 in enumerate(df2['data']):
			if d1 == d2:
				yield i, j

def loop_over_timestamps(df1, df2):
	return all(match_timestamps(df1, df2, i, j) for i, j in match_timestamps(df2, df1, i, j))
