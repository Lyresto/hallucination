# Solution 1
# Using torch.split()

a_split = torch.split(a, chunk_dim, dim=2)
tensors_31 = list(a_split)

# Solution 2
# Using torch.narrow()

tensors_31 = []
for i in range(a.shape[2] - chunk_dim + 1):
    tensor_i = a.narrow(2, i, chunk_dim)
    tensors_31.append(tensor_i)

# Solution 3
# Using numpy.split()

a_np = a.numpy()
tensors_31_np = np.split(a_np, a_np.shape[2] - chunk_dim + 1, axis=2)
tensors_31 = [torch.from_numpy(tensor_np) for tensor_np in tensors_31_np]

# Solution 4
# Using pandas.DataFrame

a_np = a.numpy()
a_df = pd.DataFrame(a_np.reshape(-1, a.shape[-2]))
tensors_31_df = [torch.from_numpy(tensor_df.values.reshape(a.shape[:2] + (chunk_dim, -1, a.shape[-1]))) for _, tensor_df in a_df.rolling(window=chunk_dim, axis=1)]
tensors_31 = [tensor.unsqueeze(3) for tensor in tensors_31_df]

# Solution 5
# Using torch.as_strided()

a_shape = a.shape
a_stride = a.stride()
chunk_stride = a_stride[2] * chunk_dim
tensors_31 = []
for i in range(a_shape[2] - chunk_dim + 1):
    tensor_i = torch.as_strided(a, (a_shape[0], a_shape[1], chunk_dim, a_shape[3], a_shape[4]), (a_stride[0], a_stride[1], chunk_stride, a_stride[3], a_stride[4]), storage_offset=a.storage_offset() + i * a_stride[2])
    tensors_31.append(tensor_i)

# Ensure the shapes of tensors
assert all(tensor.shape == (1, 3, 10, 10, 1) for tensor in tensors_31)

# Ensure the values of tensors
assert all(torch.allclose(tensor, a[:, :, i:i+chunk_dim, :, :]) for i, tensor in enumerate(tensors_31))
