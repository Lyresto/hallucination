y = torch.argmax(softmax_output, dim=1).unsqueeze(1)