# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0014_auto_20151118_0248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='name',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='author',
            name='first_name',
            field=models.CharField(null=True, max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='middle_name',
            field=models.CharField(null=True, max_length=255, blank=True),
        ),
    ]
