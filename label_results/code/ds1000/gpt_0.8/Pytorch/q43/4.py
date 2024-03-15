_, y = torch.max(softmax_output, dim=1)
y = y.unsqueeze(1)
