y = torch.argmax(softmax_output, dim=1).reshape(-1, 1)
