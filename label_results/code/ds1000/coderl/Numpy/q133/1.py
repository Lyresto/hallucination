from datetime import datetime
from itertools import product

def datetime_as_num(datetime_str):
	return datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")

def create_array(df):
	time_index = product(range(5), repeat=4)
	categories = df.columns.values
	data_frame = [[categories[col_idx], df[col_idx], time_index[col_idx]] for col_idx in range(15)]
	return np.array(data_frame).astype("float")
