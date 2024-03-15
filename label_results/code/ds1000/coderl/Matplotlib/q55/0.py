def reg_plot(tips):
	df = tips.copy()
	df['tip'], df['total_bill'] = df['tip'], df['total_bill']
	sns.jointplot('total_bill', 'tip', data=df, kind='reg')
	return plt.gcf()
