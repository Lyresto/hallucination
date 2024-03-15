from pandas import *
def load_data():
	d, X = pd.read_csv('/Users/AlexandreHu/Codewars/anaLis/data.csv'), pd.read_csv('/Users/AlexandreHu/Codewars/anaLis/input.csv')
	X = X.drop('', 1)
	X.set_index('Col1', inplace=True)
	Y = []
	for col in d.columns:
		Y.append(X[col].tolist())
	return pd.DataFrame(dict(zip(d.columns, Y)), columns=d.columns)
