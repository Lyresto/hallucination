from datetime import datetime
from itertools import zip_longest

def __starting_point():
	df = pd.DataFrame({'x': [100, 90, 80], 'y':[7, 8, 9]}, index=['abc', '3/1/1994', '9/1/1994', '3/1/1995'])
	print(df)
	print(df.index.levels[1])
	for (a, b), (c, d) in zip_longest(df.index.levels[:-1], df.index.levels[1:]):
		df.index.levels[1] = datetime.strptime(a, '%Y/%m/%d')
		df.index.levels[0] = datetime.strptime(c, '%Y/%m/%d')
	print(df.index.levels[1])
__starting_point()
