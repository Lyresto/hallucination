def load_data():
	data = np.array([[i, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
					[0.7, 0.2, 0.1, 0.2, 0.6, 0.2, 0.1],
					[0.2, 0.6, 0.2, 0.1, 0.1, 0.8, 0.1],
					[0.1, 0.1, 0.1, 0.8, 0.1, 0.8],
					[0, 0, 0, 0, 0, 0, 0, 0]], dtype=float)
	torch.from_numpy(data).cpu().cpu()
	return [torch.argmax(data, axis=-1)]
