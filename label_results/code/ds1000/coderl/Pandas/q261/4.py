import pandas as pd
import operator

def rank(df):
	rank = pd.DataFrame(index=df['ID'])
	for i, j in df.groupby('ID'):
		rank = rank.loc[j, 'TIME']
	return rank.rank(ascending=False)
