# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(verbose_name='slug', unique=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='photo',
            name='slug',
            field=models.SlugField(verbose_name='slug', unique=True, max_length=40),
        ),
    ]
