import pandas as pd
import datetime

def find_days(sp):
	print(sp)
	sp.sort_values(by='Date')
	start = datetime.datetime(2020, 2, 17)
	end = datetime.datetime(2020, 2, 18)
	days = 0
	for i in range(len(sp)):
		if start <= sp.loc[i]['Date'] <= end:
			days += 1
			start = sp.loc[i]['Date']
	return days
