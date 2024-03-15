scaler = MinMaxScaler()
new_a = scaler.fit_transform(a.reshape(-1,1)).reshape(a.shape)
return new_a
### END SOLUTION