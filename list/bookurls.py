from django.conf.urls import url

from list import bookviews

__author__ = 'justin'

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', bookviews.book_detail, name='book_detail'),
    url(r'^(?P<pk>[0-9]+)/edit$', bookviews.book_edit, name='book_edit'),
    url(r'^(?P<pk>[0-9]+)/delete$', bookviews.book_delete, name='book_delete'),
    url(r'^new/$', bookviews.book_new, name='book_new'),
]
