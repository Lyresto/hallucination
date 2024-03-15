def reg(df):
	x_mean, y_mean = df['total_bill'].mean(), df['tip'].mean()
	x = df['total_bill'].quantile(0.25)
	y = df['tip'].quantile(0.25)
	sns.jointplot('total_bill', 'tip', x, y, size=6, color='blue')
	return None

reg(tips)
