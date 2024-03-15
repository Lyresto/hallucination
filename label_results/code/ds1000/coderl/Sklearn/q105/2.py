import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def split(df):
	return train_test_split(df, test_size=0.8)

def load_data():
	df = pd.DataFrame.from_dict({k: v for k, v in zip(range(1, 82), range(1, 82)[::-1])})
	df.sort_values("date")
	return df
