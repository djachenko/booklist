# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0013_auto_20151118_0247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='last_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='middle_name',
        ),
    ]
