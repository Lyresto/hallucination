df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = pd.Series(data.target)
return df
### END SOLUTION