def f(lat = example_lat, lon = example_lon, val = example_val):
	df = pd.DataFrame({'lat':lat,'lon':lon,'val':val})
	for i,j in enumerate(lat):
		df['lat'][i] = j[0]
		df['lon'][i] = j[1]
		df['val'][i] = j[2]
	return df
