from copy import deepcopy
import pandas as pd
df = pd.DataFrame(
	{'HeaderA': [476],
     'HeaderB': [4365],
     'HeaderC': [457]})
df = deepcopy(df)
df.rename(columns={'HeaderA': 'HeaderAX', 'HeaderB': 'HeaderBX', 'HeaderC': 'HeaderCX'}, inplace=True)
