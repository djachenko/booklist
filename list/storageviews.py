from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from list.forms import StorageForm
from list.models import Storage, Book
from list.views import base_context

FORM_TITLE = "storage"


def storage_detail(request, pk):
    context = base_context(request)

    try:
        requested_storage = Storage.objects.get(pk=pk)
        books_in_storage = Book.objects.filter(storage=requested_storage)

        context["required"] = books_in_storage.count() > 0
        context["books"] = books_in_storage
    except ObjectDoesNotExist:
        requested_storage = None

    context["object"] = requested_storage

    return render(request, 'list/named_detail.html', context)


def storage_new(request):
    if request.method == "POST":
        storage_form = StorageForm(request.POST)

        if storage_form.is_valid():
            storage = storage_form.save()

            return redirect("storage_detail", pk=storage.pk)
        else:
            return redirect("booklist")
    else:
        storage_form = StorageForm()

        return render(request, 'list/named_edit.html', {
            'objectform': storage_form,
            "form_title": FORM_TITLE
        })


def storage_edit(request, pk):
    storage_instance = get_object_or_404(Storage, pk=pk)

    if request.method == "POST":
        form = StorageForm(request.POST, instance=storage_instance)

        if form.is_valid():
            storage_instance = form.save()

            return redirect('storage_detail', pk=storage_instance.pk)
    else:
        form = StorageForm(instance=storage_instance)

    return render(request, 'list/named_edit.html', {
        'objectform': form,
        "form_title": FORM_TITLE
    })


def storage_delete(request, pk):
    storage = get_object_or_404(Storage, pk=pk)

    storage.delete()

    return redirect("booklist")
