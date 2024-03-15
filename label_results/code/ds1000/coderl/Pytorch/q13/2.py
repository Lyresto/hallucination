def solve(A_log, B):
	torch.set('A_log', A_log)
	torch.set('B', B)
	C = B[:][A_log]
	return C
