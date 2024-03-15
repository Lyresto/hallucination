a_lengths = torch.arange(a.size(1)).unsqueeze(0).expand_as(a)
mask = a_lengths >= lengths.unsqueeze(1)
a[mask] = 0
