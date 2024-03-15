import numpy as np

stdMean = lambda x: np.std(np.mean(x))
result = df.groupby('b').a.agg([('mean', 'mean'), ('std', stdMean)])
result