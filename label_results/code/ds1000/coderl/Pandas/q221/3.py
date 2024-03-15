import re
from pandas import DataFrame

def __starting_point():
	df = DataFrame({'SOURCE_NAME': re.findall(r'[^\w_]+', input())})
	print(df)

__starting_point()
