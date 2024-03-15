import torch

def get_mask(lens):
    max_len = max(lens) # get the maximum sentence length
    mask = torch.zeros(len(lens), max_len) # create a tensor of zeros with size (batch_size, max_len)
    for i, length in enumerate(lens): # iterate over each sentence length
        mask[i, :length] = 1 # set the first 'length' elements in the i-th row to 1
    return mask

# example usage
lens = [3, 5, 4]
mask = get_mask(lens)
print(mask)
