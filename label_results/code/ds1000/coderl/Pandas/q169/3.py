import pandas as pd

def solve(df):
	df = df.filter(lambda x: x.all())
	return df.fillna(value='0', method='pad')
