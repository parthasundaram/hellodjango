from django.conf.urls import patterns, include, url
from django.contrib import admin
from uber import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'apis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name ='index'),
    url(r'^start_oauth$', views.start_oauth, name ='start_oauth'),
    url(r'^history$', views.history, name='history'),
    url(r'^health$', views.health, name='health'),
    url(r'^submit$', views.submit, name='submit'),
)
