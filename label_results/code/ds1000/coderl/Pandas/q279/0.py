from datetime import datetime
from collections import defaultdict
import pandas as pd

def days_from(start, end):
	d = datetime.strptime(start, '%Y-%m-%d')
	e = datetime.strptime(end, '%Y-%m-%d')
	return len([x for x in d.diff(e).index if x.weekday() == 4])


def week_length(s):
	return len([x for x in s.split('-') if x.isoweekday() == 4])

def to_milliseconds(s):
	n = 0
	for x in s.split('-'):
		n += int(x[1])*1000
	return n

# df = pd.read_csv('data.csv')
# print(days_from('2020-02-15 15:30:00', '2020-02-16 15:31:00'))
# print(days_from('2020-02-17 15:30:00', '2020-02-18 15:30:00'))
# print(days_from('2020-02-18 15:30:00', '2020-02-17 15:30:00'))
# print(days_from('2020-02-18 15:30:00', '2020-02-17 21:59:00'))
# print(days_from('2020-02-18 21:59:00', '2020-02-17 21:59:00'))
# print(to_milliseconds('2020-02-15 15:30:00'))
# print(to_milliseconds('2020-02-16 15:30:00'))
# print(to_milliseconds('2020-02-17 15:30:00'))
# print(to_milliseconds('2020-02-18 15:30:00'))
# print(to_milliseconds('2020-02-18 21:59:00'))

# df['Date'] = df['Date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
# print(df.head())
# print(df.tail())

# print(days_