from django.core.urlresolvers import reverse_lazy, reverse
from django.http import Http404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.views.generic.detail import SingleObjectMixin

from list.models import Book
from list.views import BaseContextMixin


def add_form_title(context, form_title):
    context.update({
        "form_title": form_title
    })

    return context


def build_model_breadcrumb(model):
    return [(model.__name__ + "s",
             reverse(model.__name__.lower() + "_all")
             )]


def build_object_breadcrumb(obj):
    if obj:
        res = build_model_breadcrumb(obj.__class__)
        res.append((obj.get_breadcrumb_name(), obj.get_absolute_url()))
        return res
    else:
        return None


class EntityAll(ListView, BaseContextMixin):
    paginate_by = 40
    context_object_name = "items"
    template_name = "list/named_all.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        model_name = self.model.__name__.lower()

        context[self.context_object_name] = [i for i in context[self.context_object_name] if i.detail_name()]
        context["title"] = "All %ss:" % model_name
        context["detail_url"] = "%s_detail" % model_name
        context["breadcrumbs"] = build_model_breadcrumb(self.model)

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
        if self.object:
            return self.object.book_set.all()
        else:
            return Book.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["required"] = self.get_queryset().count() > 0
        context["books"] = context["object_list"]
        context["object_type"] = self.model.__name__.lower()
        context["breadcrumbs"] = build_object_breadcrumb(self.object)

        return context


class EntityNew(CreateView):
    template_name = "list/named_edit.html"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.form_title = "New " + self.model.__name__.lower()

    def get_context_data(self, **kwargs):
        context = add_form_title(super().get_context_data(**kwargs), self.form_title)

        breadcrumbs = build_model_breadcrumb(self.model)
        breadcrumbs.append(("New", reverse(self.model.__name__.lower() + "_new")))

        context["breadcrumbs"] = breadcrumbs

        return context


class EntityEdit(UpdateView):
    template_name = "list/named_edit.html"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.form_title = "Edit " + self.model.__name__.lower()

    def get_context_data(self, **kwargs):
        context = add_form_title(super().get_context_data(**kwargs), self.form_title)

        breadcrumbs = build_object_breadcrumb(self.object)
        breadcrumbs.append(("Edit", reverse(self.model.__name__.lower() + "_edit", kwargs={"pk": self.object.pk})))

        context["breadcrumbs"] = breadcrumbs

        return context


class EntityDelete(DeleteView):
    success_url = reverse_lazy("booklist")
