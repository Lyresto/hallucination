from pandas import DataFrame
def query_dataframe(df,filter_list):
	catergory = '{}!='.format(filter_list[0])
	return df.query(catergory)
