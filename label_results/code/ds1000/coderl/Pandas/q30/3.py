import pandas as pd
df = pd.DataFrame(
	{'HeaderA': [476],
	'HeaderB': [4365],
	'HeaderC': [457]})
df2 = df.rename(columns={'HeaderA': 'HeaderAX', 'HeaderB': 'HeaderBX', 'HeaderC': 'HeaderCX'})
print(df2.columns)
