import numpy as np

A = ['inf', '33.33', '33.33', '33.37']
NA = np.asarray(A)

NA = np.where(NA == 'inf', np.nan, NA.astype(float))
AVG = np.nanmean(NA, axis=0)

AVG