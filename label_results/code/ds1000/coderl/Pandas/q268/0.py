def to_series(df):
	from datetime import datetime
	d = []
	for i,j in df.iteritems():
		d.append(datetime.strptime(i, '%Y-%m-%d'))
	return df.assign(Value=lambda a,b:sum(b)*a,Date=d)
