# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdclass', '0007_auto_20160425_0329'),
    ]

    operations = [
        migrations.AddField(
            model_name='bar',
            name='difficulty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bulge',
            name='difficulty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dust',
            name='difficulty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='edge',
            name='difficulty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='elliptical',
            name='difficulty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lens',
            name='difficulty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='merging',
            name='difficulty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='spiral',
            name='difficulty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tidal',
            name='difficulty',
            field=models.IntegerField(default=0),
        ),
    ]
