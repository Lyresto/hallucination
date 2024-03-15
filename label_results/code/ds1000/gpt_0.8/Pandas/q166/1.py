import numpy as np

result = df.groupby('a')['b'].agg(['mean', 'std'])
