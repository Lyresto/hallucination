import re

def extract_date(df, list):
	for i in range(len(list)):
		df['Date'] = re.sub(r'\d{2}-\d{2}-\d{4}', lambda m: f'{m.group(0)}-{m.group(1)}', df['Date'])
	return df['Date'][0:10]
