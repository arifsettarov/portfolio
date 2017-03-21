# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170319_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
            ],
            options={
                'db_table': 'email',
            },
        ),
    ]
