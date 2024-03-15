from sklearn.cross_validation import train_test_split
from collections import defaultdict
import numpy as np
import pandas as pd

def load_data():
	df = pd.read_csv('data.csv')
	df = df.sort_values(by='date')
	df_train, df_test = train_test_split(df, test_size=0.8)
	return df_train, df_test
