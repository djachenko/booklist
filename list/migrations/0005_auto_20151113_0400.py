# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import list.models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_auto_20151107_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to=list.models.generate_file_field),
        ),
        migrations.AlterField(
            model_name='book',
            name='last_accessed',
            field=models.DateTimeField(null=True),
        ),
    ]
