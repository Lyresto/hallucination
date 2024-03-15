import pandas as pd

df = pd.DataFrame({'x': x, 'y': y})

# Adjust the length of the legend handle to 0.3
df['z'] = df['y'].rolling(window='left').mean()
df['z'].plot(ax=df.plot(kind='line'), legend='Line')

# SOLUTION END
