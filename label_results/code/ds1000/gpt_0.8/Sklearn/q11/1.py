one_hot_encoder = OneHotEncoder()
transformed_data = one_hot_encoder.fit_transform(df_origin)

# convert the transformed data to a DataFrame
transformed_data_df = pd.DataFrame.sparse.from_spmatrix(transformed_data)
transformed_data_df.columns = one_hot_encoder.get_feature_names_out()

# concatenate the transformed data with the original dataframe
df = pd.concat([df_origin, transformed_data_df], axis=1)
