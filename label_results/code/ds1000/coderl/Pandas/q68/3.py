import pandas as pd
import numpy as np

def mask_df_with_rows(df):
	rows_mask = np.array([i for i, x in enumerate(df) if x[df.columns.get_loc('c')] > 0.5]).reshape(-1, 1)
	return df.loc[rows_mask]
