tensors_31 = []
for i in range(a.shape[2] - chunk_dim + 1):
    tensor = a[:, :, i:i+chunk_dim, :, :]
    tensors_31.append(tensor)
END SOLUTION
<code>