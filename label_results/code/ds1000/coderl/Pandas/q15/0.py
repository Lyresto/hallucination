import re
from collections import defaultdict

def extract(d, key):
	d = d.copy()
	for x in re.findall(r'[a-z]+', d['message'] or 'None'):
		v = x.split(':')
		if v[0] == key:
			d['name'][0] = v[0]
			d['status'][0] = v[1]
			d['number'][0] = int(v[2])
		elif v[0] == 'None':
			d['name'][0] = None
			d['status'][0] = None
			d['number'][0] = None
		elif v[0] == 'one':
			d['name'][0] = 'one'
			d['status'][0] = 'active'
			d['number'][0] = 10000
		elif v[0] == 'zero':
			d['name'][0] = 'zero'
			d['status'][0] = 'inactive'
			d['number'][0] = 0
	return d
