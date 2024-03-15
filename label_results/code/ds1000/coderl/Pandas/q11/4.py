import pandas as pd

def __starting_point():
	df = pd.read_csv('/home/pavel/Workbooks/2015-12-01.xls')
	print(df['datetime'].iloc[0])

__starting_point()
