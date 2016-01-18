# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_auto_20151024_0509'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='last_accessed',
            field=models.DateTimeField(null=True),
        ),
    ]
