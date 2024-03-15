import pandas as pd

def get_days(sp):
	start = '2020-02-15'
	end = '2020-02-16'
	days = []
	for i in range(1,20):
		days.append(sp[start+i].strftime('%A'))
		start = start+i+1
	days.append(sp[end].strftime('%A'))
	return days

