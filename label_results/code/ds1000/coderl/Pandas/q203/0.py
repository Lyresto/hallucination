from statistics import mean

def mean_value(frame, key):
	return mean([frame[key].max(), frame[key].min()][:-1])

def mean_columns(frame):
	return str([mean_value(frame, key) for key in frame.columns])

def mean_rows(frame):
	return str([mean_value(frame, key) for key in frame.index])

def __starting_point():
	df = pd.read_csv('input.txt', sep=' ', header=None)
	print(mean_columns(df))
	print(mean_rows(df))

__starting_point()
