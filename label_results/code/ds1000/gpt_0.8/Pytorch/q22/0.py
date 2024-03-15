mask = []
max_len = max(lens)
for length in lens:
    mask.append([1] * length + [0] * (max_len - length))
mask = torch.LongTensor(mask)
### END SOLUTION