from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'projects.views.index'),
    url(r'^projects/(?P<project_id>\d+)/$', 'projects.views.projectdisplay'),
    url(r'^submit/', 'projects.views.projectsubmit'),
    url(r'^about/', 'pennprojects.views.about'),
    url(r'^admin/', include(admin.site.urls)),
)
