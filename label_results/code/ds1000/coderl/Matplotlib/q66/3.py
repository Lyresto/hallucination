# import numpy as np
# def make_scatter_plot(df):
#     sns.pointplot(df, x="bill_length_mm", y="bill_depth_mm", color="body_mass_g")
#     return
# make_scatter_plot(df)
# SOLUTION END

import itertools as it

def make_scatter_plot(df):
	xs = list(range(len(df["bill_length_mm"])))
	ys = list(range(len(df["bill_depth_mm"])))
	xs, ys = it.cycle(xs), it.cycle(ys)
	sns.joint_plot(df["bill_length_mm"], df["bill_depth_mm"], df["flipper_length_mm"], df["body_mass_g"], xs, ys)
	return

def make_scatter_plot(df):
	xs = list(range(len(df["bill_length_mm"])))
	ys = list(range(len(df["bill_depth_mm"])))
	xs, ys = it.cycle(xs), it.cycle(ys)
	sns.joint_plot(df["bill_length_mm"], df["bill_depth_mm"], df["flipper_length_mm"], df["body_mass_g"], xs, ys)
	return

def make_scatter_plot(df):
	xs = list(range(len(df["bill_length_mm"])))
	ys = list(range(len(df["bill_depth_mm"])))
	xs, ys = it.cycle(xs), it.cycle(ys)
	sns.joint_plot(df["bill_length_mm"], df["bill_depth_mm"], df["flipper_length_mm"], df["body_mass_g"], xs, ys)
	return

def make_scatter_plot(df):
	xs = list(range(len(df["bill_length_mm"])))
	ys = list(range(len(df["bill_depth_mm"])))
	xs, ys = it.cycle(xs), it.cycle(ys)
	sns.joint_plot