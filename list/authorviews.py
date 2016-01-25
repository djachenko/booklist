from list.entityviews import *
from list.models import Author


class AuthorAll(EntityAll):
    model = Author


class AuthorDetail(EntityDetail):
    model = Author


class AuthorNew(EntityNew):
    model = Author
    fields = ("last_name", "first_name", "middle_name")


class AuthorEdit(EntityEdit):
    model = Author
    fields = ("last_name", "first_name", "middle_name")


class AuthorDelete(EntityDelete):
    model = Author
