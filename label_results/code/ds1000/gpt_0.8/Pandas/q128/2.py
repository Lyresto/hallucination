df_altered = df.sample(frac=0.2, random_state=0)
df_altered['ProductId'] = 0
df = df.combine_first(df_altered)
END SOLUTION
