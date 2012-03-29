import os, sys
from pyquery import PyQuery

keys= [
'',
'rooms',
'address',
'level',
'building',
'common',
'living',
'kitchen'
]

def mkresult(el, delimiter='td'):
	"""
	>>> el = PyQuery("<tr class='bg1'><td></td><td>1</td><td>qwerty</td></tr>")
	>>> mkresult(el)
	{'rooms': '1', 'address': 'qwerty'}
	"""
	obj = {}
	def _add(i, el):
		if i < 8:
			add(i, el)

	def add(i, el):
		key = keys[i]
		if key:
			pyel = PyQuery(el)
			obj[key] = pyel.text()

	def addbg3(i, el):
		if i > 0:
			i += 1
		if i < 8:
			add(i, el)
		
	klass = el.attr('class')
	tds = el.find(delimiter)
	if klass == 'bg1' or klass == 'bg2':
		tds.each(lambda i, el: _add(i, el))
	elif klass == 'bg3':
		tds.each(lambda i, el: addbg3(i, el))

	return obj

def find(rfrom, rto, pfrom, pto, metro):
	url = 'http://www.bn.ru/zap_fl.phtml?kkv1=%s&kkv2=%s&price1=%s&price2=%s&so1=&so2=&sk1=&sk2=&type[]=1&sorttype=0&sort_ord=0&metro[]=%s&text=' % (rfrom, rto, pfrom, pto, metro)
	pq = PyQuery(url=url, opener=lambda url: load(url))
	results = pq('table.results tr')
	header = mkresult(PyQuery(results[0]), 'th')
	data = [mkresult(PyQuery(el)) for el in results]
	return filter(None, [header]+data)

def getmetro():
	url = 'http://www.bn.ru/zap_fl_w.phtml'
	pq = PyQuery(url=url, opener=lambda url: load(url))
	options = pq('select#metro option')
	def mkobj(el):
		name = el.text()
		value = el.attr('value')
		return locals()
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
