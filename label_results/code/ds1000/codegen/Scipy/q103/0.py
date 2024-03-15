import numpy as np
from scipy import signal
arr = np.array([-624.59309896, -624.59309896, -624.59309896,
                      -625., -625., -625.,])
n = 2
result = signal.find_extrema(arr, n)
