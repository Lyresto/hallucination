df['Altered'] = False
for user in df['UserId'].unique():
    user_df = df[df['UserId'] == user]
    altered_df = user_df.sample(frac=0.2, random_state=0)
    df.loc[altered_df.index, 'Quantity'] = 0
    df.loc[altered_df.index, 'Altered'] = True
END SOLUTION
