df_origin = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})
transform_output = csr_matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

# Convert csr_matrix to pandas DataFrame
df_transform = pd.DataFrame.sparse.from_spmatrix(transform_output)

# Concatenate the original dataframe and the transformed dataframe
df = pd.concat([df_origin, df_transform], axis=1)
