df = df.groupby('UserId').apply(lambda x: x.sample(frac=0.2, random_state=0))
df['Quantity'] = df['Quantity'].apply(lambda x: 0 if x != 0 else x)
df = df.reset_index(drop=True)
