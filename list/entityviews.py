from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.views.generic.detail import SingleObjectMixin

from list.models import Book
from list.views import BaseContextMixin


def add_form_title(context, form_title):
    context.update({
        "form_title": form_title
    })

    return context


class EntityDetail(SingleObjectMixin, ListView, BaseContextMixin):
    template_name = "list/named_detail.html"
    paginate_by = 40

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=self.model.objects.all())

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.object.book_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["required"] = self.get_queryset().count() > 0
        context["books"] = context["object_list"]

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
