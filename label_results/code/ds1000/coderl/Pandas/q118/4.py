import pandas as pd

def select_rows(df, rows):
	df = df.set_index('rs')
	return df.select(rows)
