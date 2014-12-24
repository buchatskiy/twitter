from django.conf.urls import patterns, include, url
from django.contrib import admin
from twitter.views import twit
from loginsys.views import login, logout



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'homework.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', twit),
    url(r'^auth/login/$', login),
    url(r'^auth/logout/$', logout),
    url(r'^admin/', include(admin.site.urls)),
)
