from collections import defaultdict

def get_rows(df: pd.DataFrame):
	cols = ['Sp', 'Mt', 'Value']
	d = defaultdict(list)
	for col in cols:
		d[col] = []
	for i in range(len(df['Value'])):
			d[df['Value'][i]].append(i)
	for col in cols:
		d[col].sort()
		d[col].append(df['count'][d[col][-1]])
	return (df[d[cols[0]]]
			.groupby(by=cols[1], key=lambda x: min(d[x]))
			.groupby(by=cols[0], key=lambda x: d[x][0]))
