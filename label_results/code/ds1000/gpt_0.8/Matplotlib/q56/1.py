sns.jointplot(data=tips, x='total_bill', y='tip', kind='reg', scatter=False)
plt.show()