from django.conf.urls import url

from list import storageviews

__author__ = 'justin'

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', storageviews.storage_detail, name='storage_detail'),
    url(r'^(?P<pk>[0-9]+)/edit$', storageviews.storage_edit, name='storage_edit'),
    url(r'^(?P<pk>[0-9]+)/delete$', storageviews.storage_delete, name='storage_delete'),
    url(r'^new/$', storageviews.storage_new, name='storage_new'),
]
