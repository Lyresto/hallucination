def load_data():
	mask, clean_input_spectrogram, output = torch.tensor([[0,0,0,0,0,0,0]], dtype=torch.int)
	return output[0,:,:,mask==1]
