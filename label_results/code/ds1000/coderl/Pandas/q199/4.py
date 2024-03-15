import pandas as pd

df = pd.DataFrame({'row': ['00000 UNITED STATES', '01000 ALABAMA',
					 '01001 Autauga County, AL', '01003 Baldwin County, AL',
					 '01005 Barbour County, AL']})

fips = ['011001 Autauga County, AL', '011003 Baldwin County, AL',
	'011005 Barbour County, AL']

df['fips'] = fips
df['row'] = df['row'].str.split(' ')
