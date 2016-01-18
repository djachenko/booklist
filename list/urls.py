from django.conf.urls import url, include

from . import views
from django.conf.urls.static import static
from booklist import settings

__author__ = 'justin'

urlpatterns = [
    url(r'^$', views.booklist, name='booklist'),

    url(r'^book/', include('list.bookurls')),
    url(r'^storage/', include('list.storageurls')),
    url(r'^author/', include('list.authorurls')),
    url(r'^publisher/', include('list.publisherurls')),
    url(r'^import/*$', views.import_data, name="import"),
    url(r'^check$', views.check_import_state, name="check"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
