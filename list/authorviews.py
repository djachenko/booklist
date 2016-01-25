from list.entityviews import *
from list.models import Author

AUTHOR_FORM_TITLE = "author"


class AuthorAll(EntityAll):
    model = Author


class AuthorDetail(EntityDetail):
    model = Author


class AuthorNew(EntityNew):
    model = Author
    fields = ("last_name", "first_name", "middle_name")
    form_title = AUTHOR_FORM_TITLE


class AuthorEdit(EntityEdit):
    model = Author
    fields = ("last_name", "first_name", "middle_name")
    form_title = AUTHOR_FORM_TITLE


class AuthorDelete(EntityDelete):
    model = Author
