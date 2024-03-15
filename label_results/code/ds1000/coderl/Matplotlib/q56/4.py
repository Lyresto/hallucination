def regplot(tips):
	df = tips.copy()
	df = df.pivot(index='tip', values='total_bill')
	sns.jointplot(x='total_bill', y='tip', data=df)
	
regplot(tips)
plt.show()
