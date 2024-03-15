a = torch.zeros_like(a) # create a tensor of zeros with the same shape as 'a'
for i, length in enumerate(lengths):
    a[i, length:, :] = 0 # set all values after the specified length to zero
