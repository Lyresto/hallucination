from datetime import datetime
def extract_month_name_year(df):
	d = df['Date'].dt.to_period('M')
	return datetime.strptime(d.index, '%Y-%m-%d').strftime('%B'), datetime.strptime(d.index, '%Y').strftime('%d')
