_, y = torch.max(torch.tensor(softmax_output), 1)
y = y.numpy().reshape(-1, 1)
