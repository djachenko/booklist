from django.conf.urls import url

from list import authorviews

__author__ = 'justin'

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', authorviews.author_detail, name='author_detail'),
    url(r'^(?P<pk>[0-9]+)/edit$', authorviews.author_edit, name='author_edit'),
    url(r'^(?P<pk>[0-9]+)/delete$', authorviews.author_delete, name='author_delete'),
    url(r'^new/$', authorviews.author_new, name='author_new'),
]
