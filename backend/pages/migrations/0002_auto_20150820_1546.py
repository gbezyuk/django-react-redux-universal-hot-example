# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': 'page', 'ordering': ('order',), 'verbose_name_plural': 'pages'},
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(verbose_name='slug', unique=True, max_length=40),
        ),
    ]
