import pandas as pd

example_df = pd.DataFrame({'A': ['Good &AMP; bad', 'BB', 'CC', 'DD', 'Good &AMP; bad'], 'B': range(5), 'C': ['Good &AMP; bad'] * 5})

def f(df):
    df = df.apply(lambda x: x.str.replace('&AMP;', '&', regex=False))
    return df

result = f(example_df)
result