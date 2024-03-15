result = torch.bmm(data, W.unsqueeze(1).unsqueeze(1).expand(-1, 2*3, -1)).squeeze()
result = result.view(10, 2, 3)
