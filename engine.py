import os, sys, json
from pyquery import PyQuery
from logger import log

keys= [
'',
'rooms',
'address',
'level',
'building',
'common',
'living',
'kitchen',
'SU',
'',
'price',
'DU',
'entity',
'contact',
'info'
]

def getCacheFileName():
	module_path = os.path.abspath( __file__ )
	module_dir = os.path.dirname( module_path )
	return os.path.join(module_dir, 'metro_cache.txt')

def cache(fn):
	"""
	>>> @cache
	... def func(a):
	...   print 'called', a
	...   return a
	>>> func('arg1')
	called arg1
	'arg1'
	>>> func('arg1')
	'arg1'
	"""
	def _f(*args, **kwargs):
		path = getCacheFileName()
		if not os.path.exists(path):
			metro = fn(*args, **kwargs)
			data = json.dumps(metro)
			with open(path, 'w') as f:
				f.write(data)
		else:
			with open(path, 'r') as f:
				data = f.read()
				metro = json.loads(data)

		return metro
	return _f

def mkresult(el, delimiter='td'):
	"""
	>>> el = PyQuery("<tr class='bg1'><td></td><td>1</td><td>Brodway, 1</td><td>2/5</td><td>K</td><td>40</td><td>18</td><td>10</td><td>P</td><td></td><td>10</td></tr>")
	>>> mkresult(el)
	{'building': 'K', 'living': '18', 'level': '2/5', 'price': '10', 'SU': 'P', 'common': '40', 'address': 'Brodway, 1', 'kitchen': '10', 'rooms': '1'}
	>>> el = PyQuery("<tr class='bg3'><td></td><td>Brodway, 1</td><td>2/5</td><td>K</td><td>40</td><td>18</td><td>2500</td><td>AAA</td></tr>")
	>>> mkresult(el)
	{'building': 'K', 'living': '18', 'level': '2/5', 'price': '2500', 'entity': 'AAA', 'common': '40', 'address': 'Brodway, 1'}
	"""
	obj = {}
	def add(i, el):
		key = keys[i]
		if key:
			pyel = PyQuery(el)
			obj[key] = pyel.text()

	def addbg3(i, el):
		#it skips the rooms field
		if i > 0:
			i += 1
		#it skips the kitchen and SU fields
		if i > 6:
			i += 3
		#it skips the DU field
		if i > 10:
			i += 1

		add(i, el)
		
	klass = el.attr('class')
	tds = el.find(delimiter)
	if klass == 'bg1' or klass == 'bg2':
		tds.each(lambda i, el: add(i, el))
	elif klass == 'bg3':
		tds.each(lambda i, el: addbg3(i, el))

	return obj

def getSearchUrl(args):
	return 'http://www.bn.ru/zap_fl.phtml?kkv1=%s&kkv2=%s&price1=%s&price2=%s&so1=&so2=&sk1=&sk2=&type[]=1&sorttype=0&sort_ord=0&metro[]=%s&text=' \
			% (args.rfrom, args.rto, args.pfrom, args.pto, args.metro) 

def find(args):
	url = getSearchUrl(args)
	pq = PyQuery(url=url, opener=lambda url: load(url))
	results = pq('table.results tr')
	header = mkresult(PyQuery(results[0]), 'th')
	data = [mkresult(PyQuery(el)) for el in results]
	return filter(None, [header]+data)

@cache
def getmetro():
	log.info('loading metro list ...')
	url = 'http://www.bn.ru/zap_fl_w.phtml'
	pq = PyQuery(url=url, opener=lambda url: load(url))
	options = pq('select#metro option')
	def mkobj(el):
		return {
			'name': el.text(),
			'value': el.attr('value')
		}
	return [mkobj(PyQuery(el)) for el in options]

def load(url):
	r, w, e = os.popen3('curl %s' % url)
	data =  w.readlines()
	r.close()
	w.close()
	e.close()
	return "".join(data)

if __name__ == '__main__':
	import doctest
	doctest.testmod()
