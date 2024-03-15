from datetime import datetime
def date_convert(s):
	return datetime.strptime(s, '%Y-%m-%d %H:%M:%S')


def merge(left,right):
	merged = pd.merge(left,right,left_on='ID',right_on='ID')
	return merged
