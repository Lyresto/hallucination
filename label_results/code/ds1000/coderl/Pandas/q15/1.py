import re

def extract_dataframes(data):
	def expand(match):
		name, status, number, message = match.groups()
		jobs, money, wife, groups, kids = message.split(',')
		df = {f'{name}: {job}: {money}: {wife}: {groups}   {kids}': {'name': [name],
												'status': [status],
												 'number': [number],
												 'job': jobs.split(),
												'money': money.split(),
												 'wife': wife.split(),
												 'group': groups.split(),
												 'kids': kids,
												'message': []}}
		return df
	return re.sub(r'(\[)+(\w+):\s*(\w+)\s*', expand, data)
