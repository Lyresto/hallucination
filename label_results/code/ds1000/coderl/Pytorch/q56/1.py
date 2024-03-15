from itertools import zip_longest

def mask_spectrogram(mask, clean_input):
	spectrogram = clean_input
	for i in range(1, 400):
		if mask[0][i]!= 1:
			spectrogram = spectrogram[:, :, i]
	return spectrogram

def load_data():
	mask, clean_input = mask(1, 400), clean_input(1, 400)
	return list(zip_longest(*list(map(mask_spectrogram, list(range(1, 400))))))[-1]
