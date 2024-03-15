def stripplot(df):
	sns.stripplot(df, x='sex', y='bill_length_mm', y_log='species', y_range=(0, 90), color='species')
	return plt.gca()
