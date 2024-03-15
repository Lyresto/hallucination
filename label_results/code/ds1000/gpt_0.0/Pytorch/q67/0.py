result = torch.matmul(data, W.unsqueeze(-1)).squeeze(-1)
result = result.view(10, 2, 3)
