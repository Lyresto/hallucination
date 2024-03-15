import pandas as pd

def one_hot(col):
	seen = set()
	return [1 if col[i] in seen else 0 for i in range(len(col))]

def load_data():
	return pd.DataFrame(one_hot(df[col] for col in df.columns), columns=df.columns)
