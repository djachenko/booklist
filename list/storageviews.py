from list.entityviews import EntityDetail, EntityNew, EntityEdit, EntityDelete, EntityAll
from list.models import Storage, Book

STORAGE_FORM_TITLE = "storage"


class StorageAll(EntityAll):
    model = Storage


class StorageDetail(EntityDetail):
    model = Storage


class StorageNew(EntityNew):
    model = Storage
    fields = ("name",)
    form_title = STORAGE_FORM_TITLE


class StorageEdit(EntityEdit):
    model = Storage
    fields = ("name",)
    form_title = STORAGE_FORM_TITLE


class StorageDelete(EntityDelete):
    model = Storage
