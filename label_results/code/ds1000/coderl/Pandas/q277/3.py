import pandas as pd

def sort_df(df):
	df['VIM'] = df['VIM'].astype(float)
	df.sort_values('time', inplace=True)
	df.columns = pd.MultiIndex.from_tuples([('TGFb',0.1,2),('TGFb',1,2),('TGFb',0.1,24),('TGFb',1,24),('TGFb',0.1,48),('TGFb',1,48),('TGFb',0.1,6),('TGFb',1,6),('TGFb',0.1,6),('TGFb',10,6)],
												names=['treatment', 'dose', 'time'])
	return df
