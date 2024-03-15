result = torch.bmm(data, W.view(hid_dim, 1)).squeeze()
result = result.view(10, 2, 3)
