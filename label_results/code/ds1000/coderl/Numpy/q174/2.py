def f(lat = example_lat, lon = example_lon, val = example_val):
	lat_idx = 0
	lon_idx = 0
	val_idx = 0
	lat_col_order = ['lat', 'lon', 'val']
	lon_col_order = ['lon', 'val']
	df_lat = pd.DataFrame(lat)
	df_lon = pd.DataFrame(lon)
	df_val = pd.DataFrame(val)
	for i in range(3):
		for j in range(lat_val[lat_idx][0].size):
			df_lat.iloc[lat_idx, lon_col_order.index(lat_val[lat_idx][j]), val_col_order.index(lat_val[lat_idx][j + 1])] = lat_val[lat_idx][j]
			df_lon.iloc[lon_idx, lat_col_order.index(lat_val[lat_idx][j]), val_col_order.index(lat_val[lat_idx][j + 1])] = lon_val[lon_idx][j]
			df_val.iloc[val_idx, lat_col_order.index(lat_val[lat_idx][j]), val_col_order.index(lat_val[lat_idx][j + 1])] = val_val[val_idx][j]
		lat_idx += 1
		lon_idx += 1
		val_idx += 1
	return df_lat
