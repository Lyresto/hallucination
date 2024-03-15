df.loc[df['product'].isin(products), 'score'] *= 1
df.loc[~df['product'].isin(products), 'score'] *= 10
