from itertools import zip_longest

def load_data():
	t, idx = map(float, input().split())
	return tuple(map(int, list(zip_longest(*map(int, input().split())), fillvalue=0))), idx
