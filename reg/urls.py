from django.conf.urls import patterns, include, url
from django.conf import settings


urlpatterns = patterns('',
    
    url(r'^login/$','reg.views.do_login'),
    url(r'^logout/$','reg.views.do_logout'),   
)
