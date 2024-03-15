
    mask = torch.LongTensor(lens)
    mask[mask < 0] = 0
    mask[mask > 0] = 1
    return mask
    ### END SOLUTION

def load_data():
    #