data_df = pd.DataFrame(data.data, columns=data.feature_names)
data_df['target'] = data.target
return data_df