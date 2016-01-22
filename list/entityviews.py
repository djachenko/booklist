from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from list.models import Book
from list.views import BaseContextMixin


def add_form_title(context, form_title):
    context.update({
        "form_title": form_title
    })

    return context


class EntityDetail(DetailView, BaseContextMixin):
    template_name = "list/named_detail.html"

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None

    def related_books(self):
        return Book.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.object:
            books_in_storage = self.related_books()

            context["required"] = books_in_storage.count() > 0
            context["books"] = books_in_storage

        return context


class EntityNew(CreateView):
    template_name = "list/named_edit.html"
    form_title = ""

    def get_context_data(self, **kwargs):
        return add_form_title(super().get_context_data(**kwargs), self.form_title)


class EntityEdit(UpdateView):
    template_name = "list/named_edit.html"
    form_title = ""

    def get_context_data(self, **kwargs):
        return add_form_title(super().get_context_data(**kwargs), self.form_title)


class EntityDelete(DeleteView):
    success_url = reverse_lazy("booklist")
