from itertools import cycle

def get_first_first(df):
	for i in df.itertuples():
		yield i[0]

def join_dataframes(f, *args):
	for i in cycle(f):
		for j in i:
			args[0].append(j)
			args[1].append(i.next())
	return pd.DataFrame(args[0], args[1])
