def create_new_column_state(df):
	# your code here
	d = {'datetime':[],'col1':[],'col2':[],'col3':[]}
	for i in range(len(df)):
		d['datetime'].append(df['datetime'][i])
		d['col1'].append(df['col1'][i])
		d['col2'].append(df['col2'][i])
		d['col3'].append(df['col3'][i])
	d['state']=[0,0,0]
	for i in range(len(d['col2'])):
		if d['col2'][i] > 50:
			d['state'][0]+=d['col1'][i]
	for i in range(len(d['col3'])):
		if d['col3'][i] > 50:
			d['state'][1]+=d['col2'][i]
	for i in range(len(d['state'])):
		print(d['datetime'][i]+' '+d['col1'][i]+' '+d['col2'][i]+' '+d['col3'][i]+' '+str(d['state'][i]))
	return d['state'][-1]
