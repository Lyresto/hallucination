import pandas as pd
import numpy as np

def create_dataframes(a, b):
	a_b = pd.DataFrame([[(pd.Series(a[c]).values if a[c].dtype == np.dtype('O') else pd.np.nan) for c in range(2)] for a in a], columns=['one', 'two'])
	b_b = pd.DataFrame([[(pd.Series(b[c]).values if b[c].dtype == np.dtype('O') else pd.np.nan) for c in range(2)] for b in b], columns=['one', 'two'])
	return a_b, b_b
