import pandas as pd

df = pd.DataFrame({'text': ['abc', 'def', 'ghi', 'jkl']})
result = df.merge(df, on='text')
print(result)
