df_transform = pd.DataFrame.sparse.from_spmatrix(transform_output)
df = pd.concat([df_origin, df_transform], axis=1)
END SOLUTION
<code>