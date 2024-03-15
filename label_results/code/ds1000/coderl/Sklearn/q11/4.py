from scipy.sparse import csr_matrix
from pandas import DataFrame

def load_data():
	df = DataFrame.from_csv('test.csv')
	transformed = csr_matrix( (df[col] for col in df.columns) )
	return df, transformed
