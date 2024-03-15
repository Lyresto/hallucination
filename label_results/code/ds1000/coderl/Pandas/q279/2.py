from datetime import datetime

def weekdays(df):
	start = datetime(2020, 2, 15)
	end = datetime(2020, 2, 18)
	days = []
	for i, d in enumerate(df['Date']):
		if d < start or d > end:
			days.append(d.strftime("%A"))
	return days
