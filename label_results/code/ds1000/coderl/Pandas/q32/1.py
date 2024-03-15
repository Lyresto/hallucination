from itertools import zip_longest

def rename_columns(df):
	new_columns = []
	for i in range(len(df['HeaderA'])):
		for j in range(len(df['HeaderA']) - i - 1):
			if df['HeaderA'][i + 1]!= df['HeaderA'][j + 1]:
				new_columns.append(f'{df["HeaderA"][i]}{df["HeaderA"][j + 1]}')
	for j in range(len(df['HeaderB']) - i):
		for k in range(len(df['HeaderB']) - j):
			if df['HeaderB'][i + 1]!= df['HeaderB'][j + 1]:
				new_columns.append(f'{df["HeaderB"][i]}{df["HeaderB"][j + 1]}')
	for j in range(len(df['HeaderC']) - i):
		for k in range(len(df['HeaderC']) - j):
			if df['HeaderC'][i + 1]!= df['HeaderC'][j + 1]:
				new_columns.append(f'{df["HeaderC"][i]}{df["HeaderC"][j + 1]}')
	for j in range(len(df['HeaderX']) - i):
		for k in range(len(df['HeaderX']) - j):
			if df['HeaderX'][i + 1]!= df['HeaderX'][j + 1]:
				new_columns.append(f'{df["HeaderX"][i]}{df["HeaderX"][j + 1]}')
	return pd.DataFrame(new_columns)
