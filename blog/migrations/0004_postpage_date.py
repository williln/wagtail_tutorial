# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-23 18:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180222_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='postpage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.today, verbose_name='Post date'),
        ),
    ]
