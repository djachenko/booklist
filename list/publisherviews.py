from list.entityviews import EntityDetail, EntityNew, EntityEdit, EntityDelete, EntityAll
from list.models import Publisher


class PublisherAll(EntityAll):
    model = Publisher


class PublisherDetail(EntityDetail):
    model = Publisher


class PublisherNew(EntityNew):
    model = Publisher
    fields = ("name",)


class PublisherEdit(EntityEdit):
    model = Publisher
    fields = ("name",)


class PublisherDelete(EntityDelete):
    model = Publisher
