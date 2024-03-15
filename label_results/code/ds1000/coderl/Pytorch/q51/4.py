from collections import Counter


def load_data():
	# matrization and padding
	A = np.array(pd.read_csv("data/data_1.csv", index_col = 0))
	B = np.array(pd.read_csv("data/data_1.csv", index_col = 1))
	# padding
	A = A[:1000, None] + A[1000:, None]
	B = B[:1000, None] + B[1000:, None]
	# equality check
	return Counter(A) == Counter(B)
