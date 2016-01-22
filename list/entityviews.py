from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from list.models import Book
from list.views import BaseContextMixin

FORM_TITLE = "storage"


def add_common_context(context):
    context.update({
        "form_title": FORM_TITLE
    })

    return context


class EntityDetail(DetailView, BaseContextMixin):
    template_name = "list/named_detail.html"

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.object:
            books_in_storage = Book.objects.filter(storage=self.object)

            context["required"] = books_in_storage.count() > 0
            context["books"] = books_in_storage

        return context


class EntityNew(CreateView):
    template_name = "list/named_edit.html"

    def get_context_data(self, **kwargs):
        return add_common_context(super().get_context_data(**kwargs))


class StorageEdit(UpdateView):
    template_name = "list/named_edit.html"

    def get_context_data(self, **kwargs):
        return add_common_context(super().get_context_data(**kwargs))


class StorageDelete(DeleteView):
    success_url = reverse_lazy("booklist")
