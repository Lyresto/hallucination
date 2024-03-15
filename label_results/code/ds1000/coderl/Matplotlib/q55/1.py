sns.jointplot(tips, x='total_bill', y='tip', color='green')

# DON'T remove
tips.total_bill.hist(color='green', alpha=0.5)
tips.tip.hist(color='green', alpha=0.5)

# SOLUTION END
