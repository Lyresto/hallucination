from random import sample

def select(df, n):
	rows = list(df.sample(n, random_state=0))
	for i, row in enumerate(rows):
		row['Quantity'] = 0
	return df
