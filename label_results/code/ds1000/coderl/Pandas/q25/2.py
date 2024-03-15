import re

def extract(df, date):
	for i, row in enumerate(df.itertuples()):
		if row[0] == date:
			return row[1], row[2]
