from pandas import DataFrame

def convert_to_pandas(px):
	return DataFrame.from_tuples((row["index"], list(row.values())) for row in px.iterrows())
