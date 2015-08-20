# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(editable=False, db_index=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('slug', models.SlugField(max_length=40, verbose_name='slug')),
                ('is_enabled', models.BooleanField(default=True, verbose_name='is enabled')),
            ],
            options={
                'default_related_name': 'categories',
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(editable=False, db_index=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('slug', models.SlugField(max_length=40, verbose_name='slug')),
                ('is_enabled', models.BooleanField(default=True, verbose_name='is enabled')),
                ('image', filebrowser.fields.FileBrowseField(max_length=500, verbose_name='image')),
                ('categories', models.ManyToManyField(to='photos.Category', verbose_name='category')),
            ],
            options={
                'default_related_name': 'photos',
                'verbose_name': 'photo',
                'verbose_name_plural': 'photos',
            },
        ),
    ]
