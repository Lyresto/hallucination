from pandas import groupby

def groupby_user_transactions(df):
	result = []
	for user,group in groupby(df,key='user'):
		group_list = [[] for _ in range(len(group['time']))]
		for time,_ in zip(group['time'],group['amount']):
			group_list[time.index(time)].append(int(time)*int(group['user']))
		result.append(group_list)
	return result
