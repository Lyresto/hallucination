def extract_keys(message):
	keys = message.split(' ')
	columns = ['name','status', 'number', 'job','money', 'wife', 'group', 'kids']
	data = []
	for key in keys:
		if key == 'job':
			data.append(['matt', 'active', 12345, 'none', 'none', 'none', 'none'])
		elif key =='money':
			data.append(['matt', 'active', 12345, None, None, None])
		elif key == 'wife':
			data.append(['james', 'active', 23456, None, 10000, None])
		elif key == 'group':
			data.append(['adam', 'inactive', 34567, 'none', 'none', 'one'])
		elif key == 'kids':
			data.append([], ['one', 'one', 'one', 'one', 'one'])
		else:
			data.append(['none', 'none', None, None, None])
	return pd.DataFrame(data)
