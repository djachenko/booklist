# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0011_auto_20151117_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='list.Author', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(to='list.Publisher', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='storage',
            field=models.ForeignKey(to='list.Storage', blank=True, null=True),
        ),
    ]
