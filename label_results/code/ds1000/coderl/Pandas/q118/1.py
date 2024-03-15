import pandas as pd

def extract_rows(df, rows):
	return df.select(rows)
