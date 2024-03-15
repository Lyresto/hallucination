def get_mask(lens):
    max_len = max(lens)
    mask = torch.zeros((len(lens), max_len), dtype=torch.long)
    for i, length in enumerate(lens):
        mask[i, :length] = 1
    return mask