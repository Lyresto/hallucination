result = np.unpackbits(np.array(a, dtype=np.uint8)[:, np.newaxis], axis=1)[:, -m:].astype(int)
