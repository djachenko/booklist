from django.conf.urls import url

from list.storageviews import *

__author__ = 'justin'

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', StorageDetail.as_view(), name='storage_detail'),
    url(r'^(?P<pk>[0-9]+)/edit$', StorageEdit.as_view(), name='storage_edit'),
    url(r'^(?P<pk>[0-9]+)/delete$', StorageDelete.as_view(), name='storage_delete'),
    url(r'^new/$', StorageNew.as_view(), name='storage_new'),
    url(r'^all/$', StorageAll.as_view(), name='storage_all'),
]
