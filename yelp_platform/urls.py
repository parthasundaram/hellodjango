from django.conf.urls import patterns, include, url
from django.contrib import admin
from yelp_platform import views

urlpatterns = patterns('',
	# Examples:
    # url(r'^$', 'apis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^activate$', views.activate, name ='activate'),
    url(r'^deactivate$', views.deactivate, name ='deactivate'),
    url(r'^checkout_fulfillment/v2/check_availability$', views.check_availability, name='check_availability'),
    url(r'^(?P<business_id>\d+)', views.iframe_load, name='iframe_load'),
)
