import pandas as pd
import numpy as np
d = {'l':  ['left', 'right', 'left', 'right', 'left', 'right'],
	'r': ['right', 'left', 'right', 'left', 'right', 'left'],
	'v': [-1, 1, -1, 1, -1, -1]}
df = pd.DataFrame(d)
result = df.groupby('l')['v'].sum()['right']
