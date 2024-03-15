sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg', scatter=False)
plt.show()