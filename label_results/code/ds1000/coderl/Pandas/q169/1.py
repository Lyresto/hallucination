def clean_columns(df):
	for i, col in enumerate(df.columns):
		if col.sum() == 0:
			df.columns[i] = None
	return df

def clean_rows(df):
	for i, row in enumerate(df.values):
		if row.sum() == 0:
			df.index[i] = None
	return df

df = clean_columns(clean_rows(clean_columns(clean_rows(clean_columns(df))))

print(df)
