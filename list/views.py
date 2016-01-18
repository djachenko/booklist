import random
from celery.result import AsyncResult
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect
from list.forms import BookSearchForm, ImportForm
from list.models import Book, Publisher
from list.tasks import import_task


def base_context(request):
    form = BookSearchForm()

    return {
        "form": form
    }


def booklist(request):
    context = base_context(request)
    query = request.GET.get('q', None)

    if query is not None:
        form = BookSearchForm(request.GET)

        results = form.searchqueryset.all()

        if query:
            results.filter(text=query)

        results = results[:6]

        context_text = "Search results"

        context["form"] = form
    else:
        query = ""

        last = Book.objects.order_by("-last_accessed")[:3]
        results = last

        context_text = "Last books"

    context['results'] = results
    context['searchvalue'] = query
    context['context_text'] = context_text

    return render(request, 'list/main.html', context)


def import_data(request):
    task_id = ""

    context = {
        "contains_file": True
    }

    if request.method == "POST":
        form = ImportForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES["import_file"]

            context["import_file"] = file.name

            data_string = file.read()

            deserialized_objects = list(serializers.deserialize("json", data_string))

            result = import_task.delay(deserialized_objects)

            task_id = "ololo"  # result.id

            title = "Importing " #+ file.name + "..."
            context["task_id"] = task_id

        title = "Import failed"
    else:
        form = ImportForm()
        title = "Import"

    context["objectform"] = form
    context["title"] = title

    return render(request, "list/import.html", context)


def check_import_state(request):
    # job_id = request.GET["id"]

    # job = AsyncResult(job_id)
    total = random.randint(10, 114888)
    done = random.randint(0, total)

    data = {
        "done": done,
        "total": total
    }  # job.result or job.state

    return JsonResponse(data, safe=False)
