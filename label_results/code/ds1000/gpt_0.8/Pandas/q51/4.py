result = df.assign(**{'exp_'+col: df[col].apply(lambda x: math.exp(x)) for col in df.columns})
