from scipy.sparse import csr_matrix


def load_data():
	df = pd.read_csv('https://www.codewars.com/kata/291/train/100_17_of_the_One_Hot_Coding.csv')
	return df, csr_matrix(transform_output).T
