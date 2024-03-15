def load_data():
	t=list(map(float,input().split()))
	a=list(map(int,input().split()))
	torch.from_numpy(a).numpy()
	return t,a
