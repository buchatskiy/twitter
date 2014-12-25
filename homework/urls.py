from django.conf.urls import patterns, include, url
from django.contrib import admin
from twitter.views import twit, filter
from loginsys.views import login, logout, register



urlpatterns = patterns('',
    url(r'^$', twit),
    url(r'^page/(\d+)/$', twit),
    url(r'^auth/login/$', login),
    url(r'^auth/logout/$', logout),
    url(r'^auth/register/$', register),
    url(r'^filter/(\w+)/$', filter),
    url(r'^admin/', include(admin.site.urls)),
)
