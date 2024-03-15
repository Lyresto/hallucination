output = output * (1 - mask.unsqueeze(-1)) + clean_input_spectrogram * mask.unsqueeze(-1)
