One option is to convert the sparse matrix into a dense array using the toarray() method, and then create a new DataFrame with the transformed data:

<code>
transform_output_dense = transform_output.toarray()
transformed_df = pd.DataFrame(transform_output_dense, columns=transform_output.get_feature_names_out())
df = pd.concat([df_origin, transformed_df], axis=1)
