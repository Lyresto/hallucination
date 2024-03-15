df_sample = df.sample(frac=0.2, random_state=0)
df_sample['ProductId'] = 0
df_updated = pd.concat([df.drop(df_sample.index), df_sample])
df_updated