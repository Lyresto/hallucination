import pandas as pd
from datetime import datetime

def datetime_to_seconds(dt):
	return int((dt - datetime(2022, 1, 1)).total_seconds())

def seconds_to_datetime(seconds):
	return datetime.strptime(f'{seconds:06d}', '%H:%M')
