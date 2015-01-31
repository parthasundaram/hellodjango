from django.conf.urls import patterns, include, url
from django.contrib import admin
from yelp_platform import views

urlpatterns = patterns('',
	# Examples:
    # url(r'^$', 'apis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^activate$', views.activate, name ='activate'),
    url(r'^deactivate$', views.deactivate, name ='deactivate'),
)
