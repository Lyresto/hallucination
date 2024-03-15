import pandas as pd

def replace_amp(s):
	return ''.join(['Good &'+x.replace('&', '&amp;')+' bad' for x in s.split()])

df = pd.DataFrame(data={'Column':['Good &AMP; bad', 'BB', 'CC', 'DD', 'Good &LT; bad'], 'B': range(5), 'C': ['Good &GT; bad'] * 5})
df['Column'] = replace_amp(df['Column'])
