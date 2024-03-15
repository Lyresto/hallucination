df.loc[df['product'].isin(products), 'score'] *= 0.1
df.loc[~df['product'].isin(products), 'score'] *= 10
