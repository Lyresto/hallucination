import re

def extract(dct):
	return '\n'.join('{}{}{}{} {} {} {} {}'.format(
		name, status, number, job, money, wife, group, kids
	) if job or money or wife or group or kids else 'none'
		for name, status, number, job, money, wife, group, kids in dct.items()
	)
