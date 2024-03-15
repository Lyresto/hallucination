output = torch.where(mask == 1, clean_input_spectrogram, output)
