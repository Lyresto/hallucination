import re

def extract_month_name_year(df):
	for i, row in enumerate(df.iterrows()):
		date = row['Date']
		if i == 0:
			return date.split('-')[0]
		if i == 1:
			return '{0}-{1}'.format(date.split('-')[1], date.split('-')[0])
		if i == 2:
			return '{0}-{1}'.format(date.split('-')[1], date.split('-')[2])
		if i == 3:
			return '{0}-{1}'.format(date.split('-')[1], date.split('-')[2])
		if i == 4:
			return '{0}-{1}'.format(date.split('-')[2], date.split('-')[3])
