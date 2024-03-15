import pandas as pd
from itertools import zip_longest

def merge_rows(df):
	text = list(df['text'])
	return '-'.join(''.join(t) for t in zip_longest(*text, fillvalue=''))
