from datetime import datetime

def extract_month_name_year(df):
	dts = df.Date.dt.to_datetime(df['Date'])
	start_date = dts.year * 100 + dts.month
	end_date = start_date + 12 * ((dts.day - 1) // 12 + 1)
	return '{}-{}'.format(start_date.strftime('%b'), end_date.strftime('%b'))
