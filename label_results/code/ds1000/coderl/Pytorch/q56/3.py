import numpy as np
import pandas as pd
import torch

def mask(mask_tensor):
	return mask_tensor[0] == 1

def clean(clean_input_spectrogram):
	return clean_input_spectrogram[0] * mask(clean_input_spectrogram[0]) + clean_input_spectrogram[0].cumsum()[::-1]

def save_data(mask, clean_input_spectrogram, output):
	np_mask = np.ones((1, 400)).numpy() * mask
	output[0].numpy() = clean(clean_input_spectrogram[0])
	output[0].cumsum()[::-1] = clean(clean_input_spectrogram[0].cumsum())[::-1]
	return output
