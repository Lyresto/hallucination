from numpy import concatenate

def f(lat=example_lat, lon=example_lon, val=example_val):
	lat_values = concatenate((lat, lat), axis=0)
	lon_values = concatenate((lon, lon), axis=0)
	val_values = concatenate((val, val), axis=0)
	return pd.DataFrame({'lat': lat_values, 'lon': lon_values, 'val': val_values})
