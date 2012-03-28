import os
from django.conf.urls.defaults import patterns, include, url
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import views, settings

urlpatterns = patterns('',
	('^$', 'views.default'),
	(r'^proxy/$', 'views.proxy'),
	(r'^find/$', 'views.find'),
)

urlpatterns += staticfiles_urlpatterns()
