result = torch.bmm(data, W.unsqueeze(1).unsqueeze(2)).squeeze()
result = result.view(10, 2, 3)
