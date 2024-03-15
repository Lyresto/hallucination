tensors_31 = []
for i in range(a.shape[2] - chunk_dim + 1):
    tensors_31.append(a[:, :, i:i+chunk_dim, :, :])
END SOLUTION
