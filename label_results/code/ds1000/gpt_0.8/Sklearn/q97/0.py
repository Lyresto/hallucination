scaler = MinMaxScaler()
normalized_array = scaler.fit_transform(np_array.flatten().reshape(-1, 1))
new_a = normalized_array.reshape(np_array.shape)
### END SOLUTION
    return new_a