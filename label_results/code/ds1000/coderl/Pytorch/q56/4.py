def load_data():
	mask, clean_input_spectrogram, output = (torch.ones(1, 400), torch.zeros(1, 400, 161), torch.ones(1, 400, 161))
	return output[0,mask == 1,:] = clean_input_spectrogram[0,mask == 1,:]
