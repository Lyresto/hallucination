def load_data():
	df_orig, transform_output = pd.read_csv('input.csv')
	mat = csr_matrix((transform_output, (list(df_orig.columns) + list(df_orig.index.values))))
	return df_orig, mat
