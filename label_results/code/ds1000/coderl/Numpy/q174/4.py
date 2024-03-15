from pandas import DataFrame
def f(lat = example_lat, lon = example_lon, val = example_val):
	lat = [lat[i] for i in range(len(lat[0]))]
	lon = [lon[i] for i in range(len(lon[0]))]
	val = [val[i] for i in range(len(val[0]))]
	return DataFrame({'lat':lat, 'lon':lon, 'val':val})
