result = df.groupby('l')['v'].sum()
result.replace(0.0, np.nan, inplace=True)
