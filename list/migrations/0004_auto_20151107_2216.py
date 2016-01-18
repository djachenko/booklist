# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_book_last_accessed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='last_accessed',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 16, 16, 49, 439634, tzinfo=utc)),
        ),
    ]
