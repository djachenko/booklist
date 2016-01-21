from celery.result import AsyncResult
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect

from list.forms import BookSearchForm, ImportForm
from list.models import Book
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

        results = form.search()

        results = results[:6]

        context_text = "Search results"

        context["form"] = form
    else:
        query = ""

        last = Book.objects.all().order_by("-last_accessed")[:3]
        results = last

        context_text = "Last books"

        for i in last:
            context_text += i.last_accessed + " "

    context['results'] = results
    context['searchvalue'] = query
    context['context_text'] = context_text

    return render(request, 'list/main.html', context)


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
