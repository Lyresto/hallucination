mask = torch.zeros(len(lens), max(lens))
for i, length in enumerate(lens):
    mask[i, :length] = 1
return mask.long()
### END SOLUTION