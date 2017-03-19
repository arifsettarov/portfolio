# -*- coding: utf-8 -*-
#!C:/Users/arif/AppData/Local/Programs/Python/Python35-32/python.exe
# Generated by Django 1.10.6 on 2017-03-18 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=50, verbose_name='Название')),
                ('project_description', models.TextField(verbose_name='Описание')),
                ('project_image', models.ImageField(upload_to='', verbose_name='Изображение (500х500)')),
                ('project_url', models.URLField(verbose_name='GitHub URL')),
            ],
            options={
                'db_table': 'projects',
            },
        ),
    ]
