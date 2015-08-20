# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('name', models.CharField(verbose_name='name', max_length=255)),
                ('slug', models.SlugField(verbose_name='slug', max_length=40)),
                ('is_enabled', models.BooleanField(verbose_name='is enabled', default=True)),
                ('content', models.TextField(verbose_name='content')),
            ],
            options={
                'verbose_name': 'page',
                'default_related_name': 'pages',
                'verbose_name_plural': 'pages',
            },
        ),
    ]
