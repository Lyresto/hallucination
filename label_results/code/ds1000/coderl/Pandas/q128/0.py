import numpy as np
import random

def random_selection(df):
	n = len(df)
	r = df.sample(n, random_state=0).reset_index(drop=True)
	r['ProductId'] = 0
	return r
