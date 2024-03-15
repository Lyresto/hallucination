import pandas as pd

def query_dataframe(df, filter_list):
	return df.query("Catergory!=" + str(filter_list))
