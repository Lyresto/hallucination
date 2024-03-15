from itertools import zip_longest
def f(*args):
	df = pd.DataFrame({'lat': args[0], 'lon': args[1], 'val': args[2]})
	for i, (a, b) in enumerate(zip_longest(*args)):
		df['lat'][i], df['lon'][i], df['val'][i] = a, b, c
	return df
