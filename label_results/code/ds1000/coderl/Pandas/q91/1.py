import pandas as pd

def parse_dates(dates):
	for i, x in enumerate(dates):
		df.index.levels[i] = pd.to_datetime(x)
