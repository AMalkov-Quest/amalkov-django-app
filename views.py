from django.shortcuts import render_to_response
from django.http import HttpResponse
import engine
from logger import log

def default(request):
	metro_list = engine.getmetro()
	return render_to_response('default.html', locals())

class Args(object):    
	
	def __init__(self, args):
		self.args = args

	def __getattr__(self, key):
		try:
			return self.args[key]
		except KeyError, e:
			log.exception(e)

def find(request):
	args = Args(request.REQUEST)
	results = engine.find(args)
	if args.js == 'true':
		return render_to_response('results.html', locals())
	else:
		return render_to_response('find.html', locals())

