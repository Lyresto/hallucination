import pandas as pd
df1 = pd.DataFrame({'HeaderA': [476],
	'HeaderB': [4365],
	'HeaderC': [457]})
df2 = pd.DataFrame(
	{'HeaderA': [76],
	'HeaderB': [345],
	'HeaderC': [456]})
df = pd.concat([df1, df2], ignore_index=True)
df.rename(columns={'HeaderA': 'HeaderAX'}, inplace=True)
