import abc
import os
import uuid
from django.core.urlresolvers import reverse
from django.db import models


class DetailedModel(models.Model):
    class Meta:
        abstract = True

    @abc.abstractmethod
    def detail_name(self):
        pass

    @abc.abstractmethod
    def edit_url_name(self):
        pass


class Storage(DetailedModel):
    class Meta:
        ordering = ["name"]

    name = models.CharField(max_length=255)

    EDIT_URL_NAME = "storage_edit"

    def __str__(self):
        return self.name

    def detail_name(self):
        return self.name

    def edit_url_name(self):
        return Storage.EDIT_URL_NAME

    def get_absolute_url(self):
        return reverse("storage_detail", kwargs={"pk": self.pk})


class Author(DetailedModel):
    class Meta:
        ordering = ["last_name", "first_name", "middle_name"]

    first_name = models.CharField(max_length=255, null=True, blank=True)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255)

    EDIT_URL_NAME = "author_edit"

    def __str__(self):
        return self.full_name()

    def detail_name(self):
        return self.full_name()

    def edit_url_name(self):
        return Author.EDIT_URL_NAME

    def full_name(self):
        name = self.last_name

        if self.first_name:
            name += " %s" % self.first_name

            if self.middle_name:
                name += " %s" % self.middle_name

        return name

    def short_name(self):
        name = self.last_name

        if self.first_name:
            name += " %c." % self.first_name[0]

            if self.middle_name:
                name += "%c." % self.middle_name[0]

        return name


class Publisher(DetailedModel):
    class Meta:
        ordering = ["name"]

    name = models.CharField(max_length=255)

    EDIT_URL_NAME = "publisher_edit"

    def __str__(self):
        return self.name

    def edit_url_name(self):
        return Publisher.EDIT_URL_NAME

    def detail_name(self):
        return self.name


COVERS_FOLDER = "covers/"


def generate_file_field(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return os.path.join(COVERS_FOLDER, filename)


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ManyToManyField(Author, blank=True)
    publisher = models.ForeignKey(Publisher, null=True, blank=True)
    pages_amount = models.IntegerField(default=0)

    cover = models.ImageField(upload_to=generate_file_field, blank=True)

    storage = models.ForeignKey(Storage, null=True, blank=True)

    last_accessed = models.DateTimeField(null=True)

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={"pk": self.pk})
