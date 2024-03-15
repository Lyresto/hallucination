df_sample = df.sample(frac=0.2, random_state=0)
df.loc[df_sample.index, 'ProductId'] = 0
END SOLUTION

The resulting DataFrame df will be:

UserId    ProductId    Quantity
1         1            6
1         4            1
1         7            3
2         0            2
3         2            7
3         0            2