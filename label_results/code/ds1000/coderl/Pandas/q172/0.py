def fill_column(df, column):
	if column in df.columns:
		df[column] = df[column].fillna(value=0)
	else:
		df[column] = 0
	return df

def fill_rows(df):
	for row in df.values:
		row.fillna(value=0,inplace=True)
	return df
