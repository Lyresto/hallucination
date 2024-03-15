import pandas as pd

df = pd.DataFrame(
	data={'x':x, 'y':y}
)

df.plot(kind='line', x='x', y='y')
