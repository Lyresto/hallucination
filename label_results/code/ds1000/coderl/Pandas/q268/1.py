import pandas as pd

def stringify_dates(df):
	dates = []
	for index, column in df.items():
		d = index.strftime('%Y-%m-%d')
		ts = str(index.to_pydatetime()) + " " + str(column)
		dates.append(d)
	return dates
