# SOLUTION START
# TODO: Implement
df = pd.DataFrame({"x": x, "y": y})

df["y"] = df["x"].cumsum()


def non_transparent(x, y, p):
	p.set_data(x, y)
	p.plot(linestyle="solid", color="#000000")


non_transparent(df["x"], df["y"], plt.plot)

# TODO: Implement




