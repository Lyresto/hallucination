import re
def extract_year(df):
	d = df.Date.dt.to_period("M")
	return "{}-{}".format(d.year, d.month) if d.year > 0 else "{}-{}".format(d.month, d.year)
