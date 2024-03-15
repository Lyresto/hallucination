from datetime import datetime

def solve(df):
	min_date, max_date = min(df['dt']), max(df['dt'])
	min_date = datetime.strptime(min_date, '%Y-%m-%d')
	max_date = datetime.strptime(max_date, '%Y-%m-%d')
	diff = max_date - min_date
	for i in range(diff.days + 1):
		val = 0
		for d in range(diff.days + 1):
			val += df['val'][d + i]
		df['val'][diff.days + i] = val
	return df
