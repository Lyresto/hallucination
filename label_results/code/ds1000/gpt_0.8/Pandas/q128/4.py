df_sample = df.sample(frac=0.2, random_state=0)
df_sample['ProductId'] = 0
df.update(df_sample)
END SOLUTION