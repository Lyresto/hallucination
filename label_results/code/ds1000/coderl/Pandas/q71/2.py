import pandas as pd
def f(df, columns=['b', 'e']):
	s = pd.concat([df[col] for col in columns], axis=1)
	s.columns = [i for i in columns]
	return s.sum(columns=False)
