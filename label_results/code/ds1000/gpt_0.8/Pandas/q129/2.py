df_sampled = df.groupby('UserId').apply(lambda x: x.sample(frac=0.2, random_state=0))
df_sampled['Quantity'] = 0
df = pd.merge(df, df_sampled[['UserId', 'ProductId']], on=['UserId', 'ProductId'], how='left')
df['Quantity_y'].fillna(df['Quantity_x'], inplace=True)
df.drop('Quantity_x', axis=1, inplace=True)
df.rename(columns={'Quantity_y': 'Quantity'}, inplace=True)
END SOLUTION
