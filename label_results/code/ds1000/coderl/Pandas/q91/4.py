from datetime import datetime

def parse_date(index):
	for i in range(len(index)):
		index.levels[i] = datetime.strptime(index.levels[i], '%Y/%m/%d')
