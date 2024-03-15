from scipy.sparse import csr_matrix


def load_data():
	df_orig, transform_output = pd.read_csv('../../data/df_orig.csv'), csr_matrix(pd.read_csv('../../data/df_orig.csv'), nrows=0, ncols=0)
	return df_orig, transform_output
