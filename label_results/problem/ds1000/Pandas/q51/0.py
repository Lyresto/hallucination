result = df.assign(exp_A = lambda x: np.exp(x["A"]), exp_B = lambda x: np.exp(x["B"]))
