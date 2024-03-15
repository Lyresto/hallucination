def min_max_expand(df):
	for i, row in df.iterrows():
		row['dt'] = pd.to_datetime(row['dt'])
		row['val'] = row['val'].fillna(0)
	rows = [[i,j] for i,j in df.iterrows()]
	rows.sort(key = lambda x: x[1])
	first = rows[0][0]
	last = rows[-1][0]
	for i, row in rows:
		if first == row[1]:
			row[1] = 0
		elif last == row[1]:
			row[1] = row[2]
		else:
			row[1] += 1
			row[1] = row[1].strftime('%Y-%m-%d')
		if i == len(rows)-1:
			rows.append([first, last])
		else:
			rows.insert(i+1, [first, last])
	return df
