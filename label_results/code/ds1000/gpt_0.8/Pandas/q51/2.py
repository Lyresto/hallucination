result = df.assign(**{f"exp_{col}": df[col].apply(lambda x: np.exp(x)) for col in df.columns})
