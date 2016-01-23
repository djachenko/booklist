from celery.result import AsyncResult
from django.core import serializers
from django.db.models import Count
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.base import ContextMixin
from django.views.generic.edit import FormMixin
from haystack.generic_views import SearchView

from list.forms import BookSearchForm, ImportForm
from list.models import Book
from list.tasks import import_task


class BaseContextMixin(FormMixin):
    form_class = BookSearchForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["search_form"] = context["form"]
        del context["form"]

        return context


def base_context(request):
    form = BookSearchForm(request.GET)
    val = form.is_valid()

    return {
        "search_form": form
    }


class MainView(SearchView):
    context_object_name = "results"
    template_name = "list/main.html"
    form_name = "search_form"
    form_class = BookSearchForm

    def form_valid(self, form):
        if "q" in form.data:
            self.queryset = form.search()[:6]
            context_text = "Search results"
        else:
            self.queryset = Book.objects.all().annotate(null_accessed=Count('last_accessed')) \
                                .order_by("-null_accessed", "-last_accessed")[:3]
            context_text = "Last books"

        context = self.get_context_data(**{
            self.form_name: form,
            'query': form.cleaned_data.get(self.search_field),
            'object_list': self.queryset,
            "context_text": context_text
        })

        return self.render_to_response(context)


def import_data(request):
    context = {
        "contains_file": True
    }

    if request.method == "POST":
        form = ImportForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES["import_file"]

            data_string = file.read()

            deserialized_objects = list(serializers.deserialize("json", data_string))

            result = import_task.delay(deserialized_objects)

            task_id = result.id

            return redirect("/import?task=" + task_id)
        else:
            title = "Import failed"
    elif request.GET.get("task", None):
        task_id = request.GET["task"]

        return render(request, "list/import_progress.html", {
            "task_id": task_id
        })
    else:
        form = ImportForm()
        title = "Import"

    context["objectform"] = form
    context["title"] = title

    return render(request, "list/import.html", context)


def import_progress(request, task_id):
    title = "Import in progress"

    return render(request, "list/import.html", {
        "title": title,
        "task_id": task_id
    })


def check_import_state(request):
    job_id = request.GET["id"]

    job = AsyncResult(job_id)

    data = {
        "state": job.state
    }

    if job.state == "PROGRESS":
        total = job.info["total"]
        done = job.info["done"]

        data.update({
            "done": done,
            "total": total,
        })

    return JsonResponse(data, safe=False)
