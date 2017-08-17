from django.conf.urls.defaults import *
from blog import settings
from settings import PROJECT_PATH
from blog.views import *
import os
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^$','blog.views.index'),
    (r'^login$','blog.views.login'),
    (r'^register$','blog.views.register'),
    (r'^archive$','blog.views.archive'),
    (r'^taken$','blog.views.taken'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)


	
