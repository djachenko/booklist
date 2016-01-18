# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0009_auto_20151116_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='middle_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
