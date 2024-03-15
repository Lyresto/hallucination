from itertools import cycle

def create_dataframe_tuple_generators(dataframes):
	for i, df in enumerate(dataframes):
		yield tuple(df['one'].values)
		for row in df['two'].values:
			yield row

def pd_frames_iterator():
	dataframes = [
		pd.DataFrame(np.array([[1, 2], [3, 4]]), columns=['one', 'two'])
		for i in range(0, 20)
	]
	for df in create_dataframe_tuple_generators(dataframes):
		for i, r in enumerate(df):
			yield r
