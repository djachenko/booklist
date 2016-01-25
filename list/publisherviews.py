from list.entityviews import EntityDetail, EntityNew, EntityEdit, EntityDelete
from list.models import Publisher, Book

PUBLISHER_FORM_TITLE = "publisher"


class PublisherDetail(EntityDetail):
    model = Publisher


class PublisherNew(EntityNew):
    model = Publisher
    fields = ("name",)
    form_title = PUBLISHER_FORM_TITLE


class PublisherEdit(EntityEdit):
    model = Publisher
    fields = ("name",)
    form_title = PUBLISHER_FORM_TITLE


class PublisherDelete(EntityDelete):
    model = Publisher
