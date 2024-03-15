from pandas import Series, DataFrame

def aggregate(df):
	return (Series(df['amount']).groupby('user').sum().reset_index()
			.apply(list))
