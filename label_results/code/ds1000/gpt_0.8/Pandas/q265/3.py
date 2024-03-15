import pandas as pd

result = df.loc[0].equals(df.loc[8])
result = df.columns[result].tolist()
