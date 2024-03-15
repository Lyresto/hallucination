import numpy as np
import pandas as pd

def split_train_test(df):
	train, test = pd.DataFrame(), pd.DataFrame()
	for i, j in enumerate(df.index):
		if i % len(df) == 0:
			train[j] = df[i]
		else:
			test[j] = df[i]
	return train, test
