tensors_31=[]
def split_tensors(a,chunk_dim):
	a_split=torch.chunk(a,chunk_dim,dim=2)
	for i in range(len(tensors_31)):
		tensors_31[i]=list(map(lambda x: x[i],a_split))
	return tensors_31
