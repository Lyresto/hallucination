result = df.groupby('cokey').apply(lambda x: x.sort_values('A'))
