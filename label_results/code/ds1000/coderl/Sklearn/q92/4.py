import numpy as np
import pandas as pd

def transform(df):
	df['Sex'] = LabelEncoder.fit_transform(df['Sex'])
	return df
