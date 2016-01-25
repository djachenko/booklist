from django.conf.urls import url

from list.authorviews import AuthorNew, AuthorDetail, AuthorEdit, AuthorDelete, AuthorAll

__author__ = 'justin'

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', AuthorDetail.as_view(), name='author_detail'),
    url(r'^(?P<pk>[0-9]+)/edit$', AuthorEdit.as_view(), name='author_edit'),
    url(r'^(?P<pk>[0-9]+)/delete$', AuthorDelete.as_view(), name='author_delete'),
    url(r'^new/$', AuthorNew.as_view(), name='author_new'),
    url(r'^all/$', AuthorAll.as_view(), name='author_all'),
]
