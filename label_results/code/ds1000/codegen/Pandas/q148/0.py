import pandas as pd
import numpy as np


d = {'l':  ['left', 'right', 'left', 'right', 'left', 'right'],
     'r': ['right', 'left', 'right', 'left', 'right', 'left'],
     'v': [-1, 1, -1, 1, -1, np.nan]}
df = pd.DataFrame(d)
