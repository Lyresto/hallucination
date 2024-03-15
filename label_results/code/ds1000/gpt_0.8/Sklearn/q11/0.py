df_transformed = pd.DataFrame(transform_output.toarray())
df = pd.concat([df_origin, df_transformed], axis=1)
