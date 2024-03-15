def make_bar(df, col="s1"):
	df[col].plot(kind="bar", x=col, y=0)
	matplotlib.rcParams[col+"_label"] = col
	return df

def make_qux(df, col="s1"):
	df[col].plot(kind="qux", x=col, y=0)
	matplotlib.rcParams[col+"_label"] = col
	return df

def make_woz(df, col="s1"):
	df[col].plot(kind="woz", x=col, y=0)
	matplotlib.rcParams[col+"_label"] = col
	return df


df = make_bar(df, col="celltype")
df = make_qux(df, col="celltype")
df = make_woz(df, col="celltype")
