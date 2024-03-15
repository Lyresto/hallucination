import pandas as pd

result = df.columns[(df.iloc[0] == df.iloc[8]) & (df.iloc[0].isna() == df.iloc[8].isna())]
result