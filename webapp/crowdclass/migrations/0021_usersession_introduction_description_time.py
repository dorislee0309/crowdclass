# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdclass', '0020_auto_20160429_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersession',
            name='introduction_description_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
