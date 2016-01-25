from list.entityviews import EntityDetail, EntityNew, EntityEdit, EntityDelete, EntityAll
from list.models import Storage


class StorageAll(EntityAll):
    model = Storage


class StorageDetail(EntityDetail):
    model = Storage


class StorageNew(EntityNew):
    model = Storage
    fields = ("name",)


class StorageEdit(EntityEdit):
    model = Storage
    fields = ("name",)


class StorageDelete(EntityDelete):
    model = Storage
