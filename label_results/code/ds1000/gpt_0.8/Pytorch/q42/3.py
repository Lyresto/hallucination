_, y = torch.max(softmax_output, 1)
y = y.view(-1, 1)
