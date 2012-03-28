import os
from django.shortcuts import render_to_response
from django.http import HttpResponse
import urllib, urllib2

def default(request):
	return render_to_response('default.html')

def proxy(request):
	cwd = os.path.dirname(__file__)
	path = os.path.join(cwd, 'html', 'www.bn.ru.html')
	#path = os.path.join(cwd, 'html', 'zap_fl_w.phtml.html')
	f = open(path)
	data = f.read()
	return HttpResponse(data)

def find(request):
	return render_to_response('find.html')

def _proxy(request):
	configure()
	data = urllib2.urlopen('http://www.bn.ru/zap_fl_w.phtml').read()
	return HttpResponse(data)

def configure():
	proxy_handler = urllib2.ProxyHandler({'http': '10.30.34.42:8010'})
	opener = urllib2.build_opener(proxy_handler)
	urllib2.install_opener(opener)
