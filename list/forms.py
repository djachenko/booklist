from django.forms import ModelChoiceField, ModelForm, ModelMultipleChoiceField, Form, FileField
from form_utils.forms import BetterModelForm
from haystack.forms import SearchForm
from floppyforms import ClearableFileInput
from .models import Book, Storage, Author, Publisher


class StorageModelChoiceField(ModelChoiceField):
    pass
    # def label_from_instance(self, obj):
    #     return obj.name


class ImageThumbnailFileInput(ClearableFileInput):
    template_name = "list/util/image.html"


class BookForm(BetterModelForm):
    class Meta:
        model = Book
        # fields = ["name", "author", "publisher", "pages_amount", "storage", "cover"]

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


class StorageForm(ModelForm):
    class Meta:
        model = Storage
        fields = ("name",)


class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ("name",)


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ("last_name", "first_name", "middle_name")


class ImportForm(Form):
    import_file = FileField()
