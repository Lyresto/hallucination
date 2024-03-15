# df = pd.DataFrame({'row': ['00000 UNITED STATES', '01000 ALABAMA',
#                           '01001 Autauga County, AL', '01003 Baldwin County, AL',
#                           '01005 Barbour County, AL']})
# END SOLUTION

# a = df.fips.str[:].str.split(' ')
# print(a)

def split_row(df):
	df['fips'], df['row'] = (df.row.str[:].str.split(' ') +
								[df['row'].str[:].str.split(' ')[1]])
	return df
