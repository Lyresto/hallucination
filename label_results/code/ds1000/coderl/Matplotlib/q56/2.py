# SAVE AND PRACTICE: seaborn joint regression plot (kind='reg')
# do not use scatterplot, use seaborn.joint_plot to make joint plot
# SOLUTION END
# SOLUTION START
# make a seaborn joint reg plot (kind='reg') of 'total_bill' and 'tip' in the tips dataframe
# do not use scatterplot, use seaborn.joint_plot to make joint plot
# SOLUTION END
# SOLUTION START
# make a seaborn joint regression plot (kind='reg') of 'total_bill' and 'tip' in the tips dataframe
# do not use scatterplot, use seaborn.joint_plot to make joint plot
# SOLUTION END
# SOLUTION START
# make a seaborn joint regression plot (kind='reg') of 'total_bill' and 'tip' in the tips dataframe
# do not use scatterplot, use seaborn.joint_plot to make joint plot
# SOLUTION END
# SOLUTION START
# make a seaborn joint regression plot (kind='reg') of 'total_bill' and 'tip' in the tips dataframe
# do not use scatterplot, use seaborn.joint_plot to make joint plot
# SOLUTION END
# SOLUTION START
# make a seaborn joint regression plot (kind='reg') of 'total_bill' and 'tip' in the tips dataframe
# do not use scatterplot, use seaborn.joint_plot to make joint plot
# SOLUTION END

def regression_plot(x, y, kind='reg', x_label='total_bill', y_label='tip'):
	# use seaborn to make a regression plot
	p = sns.joint_plot(x, y, kind=kind, x_label=x_label, y_label=y_label)
	p.set(xlabel=x_label, ylabel=y_label)
	p.legend.get_frame().set_alpha(0.5)
	return p
