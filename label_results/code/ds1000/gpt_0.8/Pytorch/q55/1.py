tensors_31 = []

for i in range(31):
    start = i
    end = i + chunk_dim
    tensor = a[:, :, :, start:end, :]
    tensors_31.append(tensor)
END SOLUTION
