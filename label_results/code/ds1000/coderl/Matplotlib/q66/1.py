def plot_bp(df, x, y):
	df[x].plot.scatter(y=y, c="#FF6699", s=30)

def plot_bp_dpi(df, x, y):
	df[x].plot.density(y=y, c="#FF6699", s=30)

def plot_body(df, x, y):
	df[x].plot.scatter(y=y, c="#0000FF", s=30)

def plot_flipper(df, x, y):
	df[x].plot.scatter(y=y, c="#0000FF", s=30)

def plot_mass(df, x, y):
	df[x].plot.scatter(y=y, c="#0000FF", s=30)

def make_axes():
	f, (ax1, ax2) = plt.subplots(1, 2)
	df = pd.read_csv("penguins.csv")
	df.columns = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
	df = df.pivot(columns="body_mass_g", values="bill_length_mm", index="flipper_length_mm")
	make_bs(df, "bill_length_mm", y="bill_depth_mm")
	make_bs(df, "bill_depth_mm", y="bill_length_mm")
	make_bs(df, "flipper_length_mm", x="bill_depth_mm")
	make_bs(df, "body_mass_g", x="flipper_length_mm")
	make_bs(df, x="body_mass_g", y="bill_depth_mm")
	return (f, (ax1, ax2))

def make_bs(df, x, y):
	df[x].plot.scatter(y=y, c="#0000FF", s=30)

def make_body(df, x, y):
	df[x].plot.scatter(y=y, c="#0000FF", s=30)

def make