import pandas as pd
import re

def pivot_table(df):
	s = str(df.sort_values('01/01/19', axis=1))
	df['date'] = pd.to_datetime(s)
	df['value'] = df['01/01/19'].astype(int)
	df['boolean'] = df['01/01/19'].apply(lambda x: 'True' if x == True else 'False')
	s = str(df.sort_values('02/02/20', axis=1))
	df['date'] = pd.to_datetime(s)
	df['value'] = df['02/02/20'].astype(int)
	df['boolean'] = df['02/02/20'].apply(lambda x: 'False' if x == False else 'True')
	return df
