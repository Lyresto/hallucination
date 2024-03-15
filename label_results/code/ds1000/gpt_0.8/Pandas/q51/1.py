result = df.copy()
for col in df.columns:
    result[f"exp_{col}"] = df[col].apply(lambda x: math.exp(x))
