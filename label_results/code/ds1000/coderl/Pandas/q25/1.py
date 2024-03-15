import datetime

def extract_date(df, list):
	for index, row in enumerate(list):
		date = datetime.datetime.strptime(row, "%Y-%m-%d")
		period = date.dt.to_period("M")
		if index == 0:
			return date.strftime("%Y-%m-%d")
		elif 0 <= index <= 2:
			return "%s-%s %s" % (period.month, period.day, period.day)
		elif 1 <= index <= 3:
			return "%s-%s Tuesday" % (period.month, period.day)
