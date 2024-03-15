from numpy import array

def df_subset(df, x):
	r = []
	for i in df.itertuples(index=x):
		if 0.45 > i[1]:
			r.append(i[0])
	return r
