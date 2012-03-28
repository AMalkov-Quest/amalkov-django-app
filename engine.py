import os, sys
from pyquery import PyQuery

def find(rfrom, rto, pfrom, pto, metro):
	url = 'http://www.bn.ru/zap_fl.phtml?kkv1=%s&kkv2=%s&price1=%s&price2=%s&so1=&so2=&sk1=&sk2=&type[]=1&sorttype=0&sort_ord=0&metro[]=%s&text=' % (rfrom, rto, pfrom, pto, metro)
	pq = PyQuery(url=url, opener=lambda url: load(url))
	results = pq('table.results tr')
	return [PyQuery(el).text() for el in results]

def getmetro():
	url = 'http://www.bn.ru/zap_fl_w.phtml'
	pq = PyQuery(url=url, opener=lambda url: load(url))
	options = pq('select#metro option')
	#
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
	#print load('http://www.bn.ru/zap_fl_w.phtml')
	#getmetro()
	find(1, 2, 1000, 2000, 52)
