result = np.unpackbits(np.uint8(a.reshape(-1,1)), axis=1)[:, -m:]
