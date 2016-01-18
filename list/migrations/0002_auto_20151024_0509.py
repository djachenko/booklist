# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='notes',
        ),
        migrations.AddField(
            model_name='book',
            name='pages_amount',
            field=models.IntegerField(default=0),
        ),
    ]
