df.loc[df['product'].isin(products), 'score'] = df.loc[df['product'].isin(products), 'score'] * 2
df.loc[~df['product'].isin(products), 'score'] = df.loc[~df['product'].isin(products), 'score'] * 10
