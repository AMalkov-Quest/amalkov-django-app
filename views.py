from django.shortcuts import render_to_response
from django.http import HttpResponse
import engine

def default(request):
	metro_list = engine.getmetro()
	return render_to_response('default.html', locals())

def find(request):
	rfrom = request.REQUEST.get('rfrom')
	rto = request.REQUEST.get('rto')
	pfrom = request.REQUEST.get('pfrom')
	pto = request.REQUEST.get('pto')
	metro = request.REQUEST.get('metro')
	results = engine.find(rfrom, rto, pfrom, pto, metro)
	return render_to_response('find.html', locals())

