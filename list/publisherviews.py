from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from list.forms import PublisherForm
from list.models import Publisher, Book
from list.views import base_context

FORM_TITLE = "publisher"


def publisher_detail(request, pk):
    context = base_context(request)

    try:
        requested_publisher = Publisher.objects.get(pk=pk)
        books_of_publisher = Book.objects.filter(publisher=requested_publisher)

        context["required"] = books_of_publisher.count() > 0
        context["books"] = books_of_publisher
    except ObjectDoesNotExist:
        requested_publisher = None

    context["object"] = requested_publisher

    return render(request, 'list/named_detail.html', context)


def publisher_new(request):
    if request.method == "POST":
        publisher_form = PublisherForm(request.POST)

        if publisher_form.is_valid():
            publisher = publisher_form.save()

            return redirect("publisher_detail", pk=publisher.pk)
        else:
            return redirect("booklist")
    else:
        publisher_form = PublisherForm()

        return render(request, 'list/named_edit.html', {
            'objectform': publisher_form,
            "form_title": FORM_TITLE
        })


def publisher_edit(request, pk):
    publisher_instance = get_object_or_404(Publisher, pk=pk)

    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher_instance)

        if form.is_valid():
            publisher_instance = form.save()

            return redirect('publisher_detail', pk=publisher_instance.pk)
    else:
        form = PublisherForm(instance=publisher_instance)

    return render(request, 'list/named_edit.html', {
        'objectform': form,
        "form_title": FORM_TITLE
    })


def publisher_delete(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)

    publisher.delete()

    return redirect("booklist")
