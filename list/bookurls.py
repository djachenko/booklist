from django.conf.urls import url

from list.bookviews import BookDetail, BookCreate, BookEdit, BookDelete, BookAll

__author__ = 'justin'

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', BookDetail.as_view(), name='book_detail'),
    url(r'^(?P<pk>[0-9]+)/edit$', BookEdit.as_view(), name='book_edit'),
    url(r'^(?P<pk>[0-9]+)/delete$', BookDelete.as_view(), name='book_delete'),
    url(r'^new/$', BookCreate.as_view(), name='book_new'),
    url(r'^all/$', BookAll.as_view(), name='book_all'),
]
