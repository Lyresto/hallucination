# Convert csr_matrix to a pandas DataFrame
transform_output_df = pd.DataFrame.sparse.from_spmatrix(transform_output)

# Concatenate the original DataFrame and the transformed DataFrame
df = pd.concat([df_origin, transform_output_df], axis=1)
