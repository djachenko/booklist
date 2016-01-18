from django.conf.urls import url

from list import publisherviews

__author__ = 'justin'

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', publisherviews.publisher_detail, name='publisher_detail'),
    url(r'^(?P<pk>[0-9]+)/edit$', publisherviews.publisher_edit, name='publisher_edit'),
    url(r'^(?P<pk>[0-9]+)/delete$', publisherviews.publisher_delete, name='publisher_delete'),
    url(r'^new/$', publisherviews.publisher_new, name='publisher_new'),
]
