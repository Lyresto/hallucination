import pandas as pd
import re

def select(df, rows):
	print(rows)
	for row in df.index.values:
		print(row)
	rows = [row.replace('rs', '').replace(':', '') for row in rows]
	print(rows)
	return df.select(rows)
