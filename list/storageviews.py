from list.entityviews import EntityDetail, EntityNew, EntityEdit, EntityDelete
from list.models import Storage, Book

STORAGE_FORM_TITLE = "storage"


class StorageDetail(EntityDetail):
    model = Storage

    def related_books(self):
        return Book.objects.filter(storage=self.object)


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
