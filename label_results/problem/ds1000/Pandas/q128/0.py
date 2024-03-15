df_sampled = df.sample(frac=0.2, random_state=0)
df_sampled['ProductId'] = 0
df.loc[df_sampled.index] = df_sampled
