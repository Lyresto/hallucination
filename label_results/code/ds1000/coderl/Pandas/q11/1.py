import pandas as pd

def tz_localize(s):
	return s.replace('-06:00', '00:00').replace('-05:00', '00:00').replace('-04:00', '00:00').replace('-06', '00')
