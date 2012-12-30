from django.conf.urls import patterns, include, url

urlpatterns = patterns('projects.views',
    url(r'^$', 'index'),
    url(r'^(?P<project_id>\d+)/$', 'display'),
)