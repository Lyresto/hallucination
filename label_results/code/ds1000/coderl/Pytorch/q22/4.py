def get_mask(lens):
	lens = [len(lens)] * len(lens)
	return [1] * len(lens) + [0] * len(lens)
