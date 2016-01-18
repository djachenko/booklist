from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from list.forms import BookForm
from list.models import Book, Storage
from list.views import base_context


# class BookDetailView(DetailView):
#     model = Book
#     template_name = "list/book_detail.html"
#     context_object_name = "book"


def book_detail(request, pk):
    context = base_context(request)

    try:
        requested_book = Book.objects.get(pk=pk)

        requested_book.last_accessed = timezone.now()
        requested_book.save()
    except ObjectDoesNotExist:
        requested_book = None

    context["object"] = requested_book

    return render(request, 'list/book_detail.html', context)


def book_new(request):
    if request.method == "POST":
        book_form = BookForm(request.POST, request.FILES)

        if book_form.is_valid():
            book = book_form.save()

            return redirect("book_detail", pk=book.pk)
    else:
        book_form = BookForm()

    return render(request, 'list/book_edit.html', {
        'objectform': book_form,
        'contains_file': True
    })


def book_edit(request, pk):
    book_instance = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book_instance)

        if form.is_valid():
            book_instance = form.save()

            return redirect('book_detail', pk=book_instance.pk)
        else:
            return redirect("booklist")
    else:
        form = BookForm(instance=book_instance)

    return render(request, 'list/book_edit.html', {
        'objectform': form,
        'contains_file': True
    })


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    book.delete()

    return redirect("booklist")
