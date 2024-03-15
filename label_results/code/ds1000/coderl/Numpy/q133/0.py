from datetime import datetime

def to_numpy_array(df):
	df_t = df.to_dict()
	df_t["major"] = df_t["major"].astype(float)
	arr = [[df_t[str(i)][j] for j in range(5)] for i in range(15)]
	return np.array(arr)
