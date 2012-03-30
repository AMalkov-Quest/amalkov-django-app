import os
from django.conf.urls.defaults import patterns, include, url
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import views, settings

urlpatterns = patterns('',
	('^$', 'views.default'),
	(r'^find/$', 'views.find'),
)

urlpatterns += staticfiles_urlpatterns()
