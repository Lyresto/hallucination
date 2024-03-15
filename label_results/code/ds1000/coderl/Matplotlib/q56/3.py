def reg(tips):
	x,y=[tips[c] for c in 'total_bill tip'.split()]
	return (x-y)*(x+y)

tips = tips.drop("tip",1)
tips.sort_values(by=['total_bill'],inplace=True)
sns.jointplot(x='total_bill',y='tip',reg=reg, size=8)
#plt.show()
