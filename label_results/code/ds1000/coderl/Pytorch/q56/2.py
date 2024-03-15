def mask(x):
	return x & (x!= 0)

def clean_input_spectrogram(x):
	return x * (1 - mask(x))

def load_data():
	# your code here
	mask, clean_input_spectrogram, output = mask(torch.zeros(1, 400)), clean_input_spectrogram(torch.ones(1, 400)), output(torch.zeros(1, 400, 161))
	return output
