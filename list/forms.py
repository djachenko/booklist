from django.forms import ModelChoiceField, Form, FileField
from floppyforms import ClearableFileInput
from form_utils.forms import BetterModelForm
from haystack.forms import SearchForm

from .models import Book, Storage, Publisher


class StorageModelChoiceField(ModelChoiceField):
    pass
    # def label_from_instance(self, obj):
    #     return obj.name


class ImageThumbnailFileInput(ClearableFileInput):
    template_name = "list/util/image.html"


class BookForm(BetterModelForm):
    class Meta:
        model = Book

        fieldsets = [(
            "data", {
                "fields": (
                    "name",
                    "author",
                    "publisher",
                    "pages_amount",
                    "storage"
                )
            }
        ), (
            "cover", {
                "fields": (
                    "cover",
                )
            }
        )]

        widgets = {
            "cover": ImageThumbnailFileInput
        }

    storage = ModelChoiceField(Storage.objects.all(), empty_label="")
    publisher = ModelChoiceField(Publisher.objects.all(), empty_label="", required=False)


class BookSearchForm(SearchForm):
    def no_query_found(self):
        return self.searchqueryset.all()


class ImportForm(Form):
    import_file = FileField()
