from pandas import defaultdict

def rank_table(df):
	d = defaultdict(list)
	for i, x in enumerate(df['TIME']):
		d[int(x)].append(i)
	for k, v in d.items():
		v.sort()
	return df.groupby('ID')['TIME'].rank(ascending=False).to_dict()
