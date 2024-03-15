_, y = torch.max(softmax_output, dim=1)
y = y.view(-1, 1)
