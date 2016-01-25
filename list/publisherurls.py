from django.conf.urls import url

from list.publisherviews import *

__author__ = 'justin'

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', PublisherDetail.as_view(), name='publisher_detail'),
    url(r'^(?P<pk>[0-9]+)/edit$', PublisherEdit.as_view(), name='publisher_edit'),
    url(r'^(?P<pk>[0-9]+)/delete$', PublisherDelete.as_view(), name='publisher_delete'),
    url(r'^new/$', PublisherNew.as_view(), name='publisher_new'),
    url(r'^all/$', PublisherAll.as_view(), name='publisher_all'),
]
