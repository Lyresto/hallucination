import numpy as np
import pandas as pd

def cycle(df):
	it = iter(df.iterrows())
	return list(zip(*(next(it) for _ in range(len(df.columns)))))


# print(cycle(a))
# print(cycle(b))
# print(cycle(c))
