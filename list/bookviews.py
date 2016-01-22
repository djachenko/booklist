from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.utils import timezone
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from list.forms import BookForm
from list.models import Book
from list.views import BaseContextMixin


def enable_cover_field(context):
    context["contains_file"] = True
    return context


class BookDetail(DetailView, BaseContextMixin):
    model = Book
    template_name = "list/book_detail.html"
    context_object_name = "object"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_object(self, queryset=None):
        try:
            requested_book = super().get_object(queryset)

            requested_book.last_accessed = timezone.now()
            requested_book.save()

            return requested_book
        except Http404:
            return None


class BookCreate(CreateView, BaseContextMixin):
    model = Book
    form_class = BookForm
    template_name = "list/book_edit.html"

    def get_context_data(self, **kwargs):
        return enable_cover_field(super().get_context_data(**kwargs))


class BookEdit(UpdateView, BaseContextMixin):
    model = Book
    form_class = BookForm
    template_name = "list/book_edit.html"

    def get_context_data(self, **kwargs):
        return enable_cover_field(super().get_context_data(**kwargs))


class BookDelete(DeleteView, BaseContextMixin):
    model = Book
    success_url = reverse_lazy("booklist")
