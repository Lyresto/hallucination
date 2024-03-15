from itertools import count

def index_select(*args):
	i, c = args
	return i[i] if isinstance(i, int) else torch.LongTensor(zip(*args))[:i]
