import datetime as dt
from itertools import chain, zip_longest

def parse_date(dates):
	for i, d in zip_longest(*zip_longest(*[iter(dates)] * 2)):
		try:
			i = dt.strptime(d, '%Y/%m/%d')
			yield i
		except ValueError:
			pass

def __starting_point():
	df = pd.DataFrame({'x': [100, 90, 80], 'y':[7, 8, 9]}, index=['abc', '3/1/1994', '3/1/1995'])
	print(df.index.levels[1])
	for i, j in parse_date(df.index.levels[1]):
		print(i, j)
	print(df.index.levels[1])

__starting_point()
