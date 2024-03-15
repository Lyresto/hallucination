import pandas as pd

x_series = pd.Series(x)
y_series = pd.Series(y)

x_series.plot(kind='line', x='x')
y_series.plot(kind='line', x='x')

# SOLUTION END
