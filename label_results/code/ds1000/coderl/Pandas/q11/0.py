import pandas as pd

def tz_localize(datetime):
	t = datetime.split(' ')
	s = str(t[0]) +'' + t[1][:2] +'' + t[1][3:]
	t[0] = s[:-3]
	t[1] = s[-3:]
	return pd.to_datetime(t)
