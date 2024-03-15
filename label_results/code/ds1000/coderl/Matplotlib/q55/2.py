def regplot(df):
	sns.jointplot(x='total_bill', y='tip', reg=df, kind='reg')
	# set y-axis labels
	if not df.empty:
		sns.jointplot(x='total_bill', y='tip', reg=df, kind='reg', y_fmt='%1.1f')
	return plt.gcf()
