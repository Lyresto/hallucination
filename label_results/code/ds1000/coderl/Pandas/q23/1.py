from datetime import datetime
def extract_month_name_year(df):
	return datetime.strptime(df['Date'], '%Y-%m-%d').strftime('%b'), datetime.strptime(df['Date'],'%Y').strftime('%d')
