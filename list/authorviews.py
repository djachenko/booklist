from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404

from list.forms import AuthorForm
from list.models import Author
from list.views import base_context

FORM_TITLE = "author"

def author_detail(request, pk):
    context = base_context(request)

    try:
        requested_author = Author.objects.get(pk=pk)

        authors_books = requested_author.book_set.all()
        context["books"] = authors_books
    except ObjectDoesNotExist:
        requested_author = None

    context["object"] = requested_author

    return render(request, 'list/named_detail.html', context)


def author_new(request):
    if request.method == "POST":
        author_form = AuthorForm(request.POST)

        if author_form.is_valid():
            author = author_form.save()

            return redirect("author_detail", pk=author.pk)
        else:
            return redirect("booklist")
    else:
        author_form = AuthorForm()

        return render(request, 'list/named_edit.html', {
            'objectform': author_form,
            "form_title": FORM_TITLE
        })


def author_edit(request, pk):
    author_instance = get_object_or_404(Author, pk=pk)

    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author_instance)

        if form.is_valid():
            author_instance = form.save()

            return redirect('author_detail', pk=author_instance.pk)
    else:
        form = AuthorForm(instance=author_instance)

    return render(request, 'list/named_edit.html', {
        'objectform': form,
        "form_title": FORM_TITLE
    })


def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)

    author.delete()

    return redirect("booklist")
