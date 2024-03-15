from datetime import datetime as dt
from datetime import timedelta as dt
import pandas as pd

def get_date_range(start, end):
	start = dt.strptime(start, "%Y-%m-%d")
	end = dt.strptime(end, "%Y-%m-%d")
	delta = (end - start).days
	return (start + timedelta(delta))[:-delta]
	
	
def get_days(sp):
	sp.index = pd.to_datetime(sp.index, unit='s')
	days = []
	for i in range(len(sp)):
		if (sp.index.year == i + 1) & (sp.index.month == i + 1) & (sp.index.day == i + 1):
			days.append(str(sp.index.day))
	return days
